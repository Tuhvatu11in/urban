from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

# Замените токен на свой
API_TOKEN = "YOUR_TOKEN_HERE"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """
    Печатает приветственное сообщение при команде /start.
    """
    await message.answer("Привет! Я бот помогающий твоему здоровью.")
    print("Пользователь начал общение.")

@dp.message_handler()
async def all_messages(message: types.Message):
    """
    Печатает сообщение о необходимости ввести /start при любом другом сообщении.
    """
    await message.answer("Введите команду /start, чтобы начать общение.")
    print("Пользователь ввёл:", message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
