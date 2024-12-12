import json
from json import JSONDecodeError


def load_transactions(file_path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            date = json.load(f)
            if not isinstance(date, list):
                return []
            return date
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []


print(load_transactions("/Users/krynik/PycharmProjects/bank_vidget/data/operations.json"))
