from requests import get
from bs4 import BeautifulSoup
from aiogram.types import Message


def alg9mp(number: int, message: Message) -> str:
    try:
        response = get(f"https://gdz.ru/class-9/algebra/merzlyak/{number}-nom/")
        soup = BeautifulSoup(response.text, 'lxml')
        url = "https:" + str(soup.find("img", attrs={'alt': f"ГДЗ по алгебре 9 класс  Мерзляк   упражнение - {number}, Решебник к учебнику 2021"})).replace('" title=""/>', '').split('src="')[1]
        return url
    except Exception as e:
        with open("logs.txt", "a") as file:
            file.write(f"[ERROR] ({message.date}) - {e}\n")
        return ""

def geo9mp(number: int, message: Message) -> str:
    try:
        response = get(f"https://gdz.ru/class-9/geometria/merzlyak-polonskij/{number}-nom/")
        soup = BeautifulSoup(response.text, 'lxml')
        url = "https:" + str(soup.find("img", attrs={'alt': f"ГДЗ по геометрии 9 класс  Мерзляк   упражнение - {number}, Решебник"})).replace('" title=""/>', '').split('src="')[1]
        return url
    except Exception as e:
        with open("logs.txt", "a") as file:
            file.write(f"[ERROR] ({message.date}) - {e}\n")
        return ""

def rus9bl(number: int, message: Message) -> str:
    try:
        response = get(f"https://gdz.ru/class-9/russkii_yazik/barhudarov-kruchkov-9/{number}-nom/")
        soup = BeautifulSoup(response.text, 'lxml')
        url = "https:" + str(soup.find("img", attrs={'alt': f"ГДЗ по русскому языку 9 класс  Бархударов   упражнение - {number}, Решебник к учебнику 2019"})).replace('" title=""/>', '').split('src="')[1]
        return url
    except Exception as e:
        with open("logs.txt", "a") as file:
            file.write(f"[ERROR] ({message.date}) - {e}\n")
        return ""