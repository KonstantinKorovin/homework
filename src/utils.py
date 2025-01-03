import json
import logging
from json import JSONDecodeError

utils_loger = logging.getLogger("utils")
file_handler = logging.FileHandler("/Users/krynik/PycharmProjects/bank_vidget/logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_loger.addHandler(file_handler)
utils_loger.setLevel(logging.DEBUG)


def load_transactions(file_path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    utils_loger.info("Starting app..")
    try:
        utils_loger.info("Initialization..")
        with open(file_path, "r") as f:
            utils_loger.info("Loading..")
            date = json.load(f)
            if not isinstance(date, list):
                utils_loger.debug("Are you sure the list exists?")
                utils_loger.info("Finished app")
                return []
            utils_loger.info("Success!")
            utils_loger.info("Finished app")
            return date
    except FileNotFoundError:
        utils_loger.debug("Are you sure the file exists?")
        utils_loger.info("Finished app")
        return []
    except JSONDecodeError:
        utils_loger.error("JSONDecodeError!")
        utils_loger.info("Finished app")
        return []
