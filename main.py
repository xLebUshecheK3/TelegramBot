import logging
import get
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from time import time, gmtime


# Настрока логирования
logging.basicConfig(level=logging.INFO)

# Создание объекта бота и диспетчера для него
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def get_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=4)
    buttons = [
        "📘 Алгебра 📘",
        "📙 Геометрия 📙",
        "📕 Русский язык 📕",
        "📚 Физика 📚",
        "📘 Алгебра - Дидактические материалы 📖",
        "📙 Геометрия - Дидактические материалы 📖",
        "📒 Английский язык 📒",
        "📗 Химия 📗"
    ]
    keyboard.add(*buttons)
    return keyboard

# Стартовая команда, выбор предметов
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Выберите предмет, для которого вы хотите найти ответы", reply_markup=get_keyboard())

# Выбор класса для алгебры
@dp.message_handler(lambda message: message.text == "📘 Алгебра 📘")
async def algebra(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="9 класс", callback_data="alg9"))
    await message.answer("Выберите класс", reply_markup=keyboard)

# Выбор автора учебника
@dp.callback_query_handler(text="alg9")
async def author(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Мерзляк, Полонский", callback_data="alg9mp"))
    await call.message.edit_text("Выберите автора", reply_markup=keyboard)
    await call.answer()

# Выбор номер задания
@dp.callback_query_handler(text="alg9mp")
async def number(call: types.CallbackQuery):
    await call.message.edit_text("Укажите номер задания")
    await call.answer()

# Парсинг фотографии и отправка пользователю
@dp.message_handler(lambda message: int(message.text) in (i for i in range(1, 2000)))
async def post(message: types.Message):
    response = get.alg9mp(int(message.text))
    if response:
        await message.answer_photo(response, reply_markup=get_keyboard())
        # Логирование
        with open("logs.txt", "a") as file:
            t = gmtime(time() + 10800)
            file.write(f"[INFO] ({t.tm_mday}.{t.tm_mon}.{t.tm_year} {t.tm_hour}:{t.tm_min}:{t.tm_sec}) - {message.from_user.id}, alg9mp\n")
    else:
        await message.answer("Произошла неизвестная ошибка")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
