from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Замените на ваш токен
API_TOKEN = '7329119208:AAFmePcGdKlgDr6bq7SPQiJ-VU8M6Owwi3Y'

# Инициализируйте бота и диспетчер с MemoryStorage
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Определение группы состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Обработчик для начальной команды 'Calories'
@dp.message_handler(commands=['start'], state=None)
async def start_command(message: types.Message):
    # Создаем клавиатуру
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = types.KeyboardButton('Рассчитать')
    button_info = types.KeyboardButton('Информация')
    keyboard.add(button_calculate, button_info)

    await message.answer("Привет! Давай рассчитаем твою норму калорий.", reply_markup=keyboard)

# Функция для установки возраста
@dp.message_handler(text='Рассчитать', state=None)
async def set_age(message: types.Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)

# Функция для установки роста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await state.set_state(UserState.growth)

# Функция для установки веса
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await state.set_state(UserState.weight)

# Функция для расчета и отправки нормы калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула Миффлина - Сан Жеора для мужчин
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша примерная норма калорий: {calories}")

    await state.finish()

# Обработчик кнопки 'Информация' (добавлено)
@dp.message_handler(text='Информация', state=None)
async def send_info(message: types.Message):
    await message.answer("Здесь будет информация о расчете калорий.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
