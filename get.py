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

def alg_dm9mp(seq: str, message: Message) -> str:
    choice, variant, number = seq.split(":")[1].split(",")
    tmp = {"var": ' ', "kontrol": " контрольная работа / "}
    try:
        response = get(f"https://gdz.ru/class-9/algebra/didakticheskie-materiali-merzlyak/{variant}-{choice}-{number}/")
        soup = BeautifulSoup(response.text, 'lxml')
        url = "https:" + str(soup.find("img", attrs={'alt': f"ГДЗ по алгебре 9 класс Мерзляк дидактические материалы {tmp[choice]}вариант {variant} - {number}, Решебник"})).replace('" title=""/>', '').split('src="')[1]
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

def geo_dm9mp(seq: str, message: Message) -> str:
    choice, variant, number = seq.split(":")[1].split(",")
    tmp = {"var": ' ', "kontrol": " контрольная работа / "}
    try:
        response = get(f"https://gdz.ru/class-9/geometria/didakticheskie-materiali-merzlyak/{variant}-{choice}-{number}/")
        soup = BeautifulSoup(response.text, 'lxml')
        url = soup.find_all("img", attrs={'alt': f"ГДЗ по геометрии 9 класс Мерзляк дидактические материалы {tmp[choice]}вариант {variant} - {number}, Решебник"})
        for item in url:
            print("\n" + str(item) + "\n")
        return "https://gdz.ru/attachments/images/tasks/000/035/926/0002/5ae195a9a67b0.jpg"
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