import json
import os
from json import JSONDecodeError


def load_transactions(list_transactions: str) -> list:
    ''' Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях '''
    try:
        with open(file_path, "r") as f:
            date = json.load(f)
            if not isinstance(date, list):
                return []
            return date
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []


base_dir = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(base_dir, "..", "data")
file_path = os.path.join(data_dir, os.path.basename("operations.json"))
print(load_transactions(file_path))

