from requests import get
from bs4 import BeautifulSoup


def alg9mp(number: int) -> str:
    try:
        responce = get(f"https://gdz.ru/class-9/algebra/merzlyak/{number}-nom/")
        soup = BeautifulSoup(responce.text, 'lxml')
        url = "https:" + str(soup.find("img", attrs={'alt': f"ГДЗ по алгебре 9 класс  Мерзляк   упражнение - {number}, Решебник к учебнику 2021"})).replace('" title=""/>', '').split('src="')[1]
        return url
    except Exception as e:
        with open("logs.txt", "a") as file:
            file.write(f"[ERROR] {e}\n")
        return ""
