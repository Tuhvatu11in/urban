from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import crud_functions

API_TOKEN = '7329119208:AAFmePcGdKlgDr6bq7SPQiJ-VU8M6Owwi3Y'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
crud_functions.initiate_db()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'], state=None)
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = types.KeyboardButton('Рассчитать')
    button_info = types.KeyboardButton('Информация')
    button_buy = types.KeyboardButton('Купить')
    keyboard.add(button_calculate, button_info, button_buy)

    await message.answer("Привет! Давай рассчитаем твою норму калорий.", reply_markup=keyboard)


@dp.message_handler(text='Купить', state=None)
async def show_buying_list(message: types.Message):
    await message.answer("Наши продукты:")

    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(
        text='Product1', callback_data='product_buying1'
    )
    button2 = types.InlineKeyboardButton(
        text='Product2', callback_data='product_buying2'
    )
    button3 = types.InlineKeyboardButton(
        text='Product3', callback_data='product_buying3'
    )
    button4 = types.InlineKeyboardButton(
        text='Product4', callback_data='product_buying4'
    )
    inline_keyboard.add(button1, button2, button3, button4)

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard)


@dp.callback_query_handler(text_startswith='product_buying')
async def handle_product_buying(call: types.CallbackQuery, state: FSMContext):
    await call.answer()

    product_id = call.data.split('_')[-1]

    await call.message.answer(
        f'Вы выбрали Product{product_id}. Описание: описание {product_id}. Цена: {product_id * 100}')
    await call.message.answer("Вы успешно приобрели продукт!")

    await state.finish()


@dp.message_handler(text='Рассчитать', state=None)
async def main_menu(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    button_calculate_calories = types.InlineKeyboardButton(
        text='Рассчитать норму калорий', callback_data='calories'
    )
    button_formulas = types.InlineKeyboardButton(
        text='Формулы расчёта', callback_data='formulas'
    )
    inline_keyboard.add(button_calculate_calories, button_formulas)

    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора: (10 * вес) + (6.25 * рост) - (5 * возраст) + 5")

@dp.callback_query_handler(text='calories', state=None)
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await state.set_state(UserState.growth)

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await state.set_state(UserState.weight)

@dp.message_handler(state=UserState.weight)
async def calculate_calories(message: types.Message, state: FSMContext):
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(message.text)

    calories = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    await message.answer(f"Ваша норма калорий: {calories}")

    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
