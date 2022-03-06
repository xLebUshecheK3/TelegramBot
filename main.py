import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
