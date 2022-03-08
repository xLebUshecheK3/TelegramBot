import logging
import get
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

# Список, хранящий id пользователя и его текущий запрос - (id, seq)
sessions = []

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

# Выбор класса для геометрии
@dp.message_handler(lambda message: message.text == "📙 Геометрия 📙")
async def geometry(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="9 класс", callback_data="geo9"))
    await message.answer("Выберите класс", reply_markup=keyboard)

# Выбор класса для русского языка
@dp.message_handler(lambda message: message.text == "📕 Русский язык 📕")
async def russian(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="9 класс", callback_data="rus9"))
    await message.answer("Выберите класс", reply_markup=keyboard)

# Выбор автора учебника для алгебры 9 класса
@dp.callback_query_handler(text="alg9")
async def author_alg9(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Мерзляк, Полонский", callback_data="alg9mp"))
    await call.message.edit_text("Выберите автора", reply_markup=keyboard)
    await call.answer()

# Выбор автора учебника для геометрии 9 класса
@dp.callback_query_handler(text="geo9")
async def author_geo9(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Мезрляк, Полонский", callback_data="geo9mp"))
    await call.message.edit_text("Выберите автора", reply_markup=keyboard)
    await call.answer()

# Выбор автора учебника для русского языка 9 класса
@dp.callback_query_handler(text="rus9")
async def author_rus9(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Бархударов, Ладыженская", callback_data="rus9bl"))
    await call.message.edit_text("Выберите автора", reply_markup=keyboard)
    await call.answer()

# Выбор номера задания для алгебры 9 класса Мерзляк, Полоснкий
@dp.callback_query_handler(text="alg9mp")
async def number_alg9mp(call: types.CallbackQuery):
    await call.message.edit_text("Укажите номер задания")
    sessions.append((call.message.chat.id, "alg9mp"))
    await call.answer()

# Выбор номера задания для геометрии 9 класса Мерзляк, Полонский
@dp.callback_query_handler(text="geo9mp")
async def number_geo9mp(call: types.CallbackQuery):
    await call.message.edit_text("Укажите номер задания")
    sessions.append((call.message.chat.id, "geo9mp"))
    await call.answer()

# Выбор номера задания для русского языка 9 класса Бархударов, Ладыженская
@dp.callback_query_handler(text="rus9bl")
async def number_rus9bl(call: types.CallbackQuery):
    await call.message.edit_text("Укажите номер задания")
    sessions.append((call.message.chat.id, "rus9bl"))
    await call.answer()

# Парсинг фотографии ответа и отправка пользователю
@dp.message_handler(lambda message: int(message.text) in (i for i in range(1, 2000)))
async def post_alg9mp(message: types.Message):
    if tuple([message.chat.id, "alg9mp"]) in sessions:
        response = get.alg9mp(int(message.text), message)
        if response:
            await message.answer_photo(response, reply_markup=get_keyboard())
            sessions.pop(sessions.index((message.chat.id, "alg9mp")))
            # Логирование
            with open("logs.txt", "a") as file:
                file.write(f"[INFO] ({message.date}) - {message.chat.id}, alg9mp\n")
        else:
            await message.answer("Произошла неизвестная ошибка")
    elif tuple([message.chat.id, "geo9mp"]) in sessions:
        response = get.geo9mp(int(message.text), message)
        if response:
            await message.answer_photo(response, reply_markup=get_keyboard())
            sessions.pop(sessions.index((message.chat.id, "geo9mp")))
            # Логирование
            with open("logs.txt", "a") as file:
                file.write(f"[INFO] ({message.date}) - {message.chat.id}, geo9mp\n")
        else:
            await message.answer("Произошла неизвестная ошибка")
    elif tuple([message.chat.id, "rus9bl"]) in sessions:
        response = get.rus9bl(int(message.text), message)
        if response:
            await message.answer_photo(response, reply_markup=get_keyboard())
            sessions.pop(sessions.index((message.chat.id, "rus9bl")))
            #Логирование
            with open("logs.txt", "a") as file:
                file.write(f"[INFO] ({message.date}) - {message.chat.id}, rus9bl\n")
        else:
            await message.answer("Произошла неизвестная ошибка")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
