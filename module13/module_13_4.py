from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Замените на ваш токен
API_TOKEN = '7329119208:AAFmePcGdKlgDr6bq7SPQiJ-VU8M6Owwi3Y'


bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Определение группы состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Обработчик для начальной команды 'Calories'
@dp.message_handler(commands=['start'], state=None)
async def start_command(message: types.Message):
    await message.answer("Привет! Давай рассчитаем твою норму калорий. Напиши 'Calories' для начала.")

# Функция для установки возраста
@dp.message_handler(text='Calories', state=None)
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

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
