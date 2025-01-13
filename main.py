import os
import re
import time

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.transactions_read import (
    reading_csv_transactions,
    reading_excel_transactions,
    reading_transactions_in_str,
    transactions_avg,
)
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

# Получаем путь к текущему файлу (main.py)
current_file = os.path.abspath(__file__)

# Получаем путь к папке src
src_dir = os.path.dirname(current_file)

# Получаем путь к папке data (находится на одном уровне с src)
data_dir = os.path.join(os.path.dirname(src_dir), "bank_vidget", "data")

# Получаем пути к файлам
PATH_TO_JSON = os.path.join(data_dir, "operations.json")
PATH_TO_CSV = os.path.join(data_dir, "transactions.csv")
PATH_TO_XLSX = os.path.join(data_dir, "transactions_excel.xlsx")

file_counter = 0


def user_file_input(user_file: str) -> list:
    ''' Функция выборки файла '''
    global file_counter
    if user_file == "1":
        print("Для обработки выбран JSON-файл")
        file_counter = 1
        return load_transactions(PATH_TO_JSON)
    elif user_file == "2":
        print("Для обработки выбран CSV-файл")
        file_counter = 2
        return reading_csv_transactions(PATH_TO_CSV)
    elif user_file == "3":
        print("Для обработки выбран XLSX-файл")
        file_counter = 3
        return reading_excel_transactions(PATH_TO_XLSX)
    return []


def user_status_input(list_transaction: list, user_status: str) -> list:
    ''' Функция выборки статуса операции '''
    if re.fullmatch("EXECUTED", user_status.replace(" ", ""), flags=re.I):
        status_transactions = filter_by_state(list_transaction, "EXECUTED")
        if status_transactions:
            print('Операции отфильтрованы по статусу "EXECUTED"')
            return status_transactions
    elif re.fullmatch("CANCELED", user_status.replace(" ", ""), flags=re.I):
        status_transactions = filter_by_state(list_transaction, "CANCELED")
        if status_transactions:
            print('Операции отфильтрованы по статусу "CANCELED"')
            return status_transactions
    elif re.fullmatch("PENDING", user_status.replace(" ", ""), flags=re.I):
        status_transactions = filter_by_state(list_transaction, "PENDING")
        if status_transactions:
            print('Операции отфильтрованы по статусу "PENDING"')
            return status_transactions
    return []


def sorted_file_input(list_status: list, user_sorted: str) -> list:
    ''' Функция сортировки по дате '''
    if re.fullmatch("Нет".replace(" ", ""), user_sorted, flags=re.I):
        return list_status
    elif re.fullmatch("Да".replace(" ", ""), user_sorted, flags=re.I):
        while True:
            print('Отсортировать "по возрастанию" или "по убыванию"?')
            ascending_input = input()
            if re.fullmatch("по возрастанию", ascending_input, flags=re.I):
                return sort_by_date(list_status, False)
            elif re.fullmatch("по убыванию", ascending_input, flags=re.I):
                return sort_by_date(list_status, True)
            else:
                print('Введите "по возрастанию" / "по убыванию"!')
    return []


def value_file_input(list_sorted: list, user_value: str) -> list:
    ''' Функция сортировки по валюте '''
    if re.fullmatch("Нет".replace(" ", ""), user_value, flags=re.I):
        return list_sorted
    elif re.fullmatch("Да".replace(" ", ""), user_value, flags=re.I) and file_counter == 1:
        return list(filter_by_currency(list_sorted, "RUB", False))
    elif re.fullmatch("Да".replace(" ", ""), user_value, flags=re.I) and file_counter in [2, 3]:
        return list(filter_by_currency(list_sorted, "RUB", True))
    return []


def word_file_input(list_value: list, user_word: str) -> list:
    ''' Функция сортировки по словву  '''
    if re.fullmatch("Нет", user_word, flags=re.I):
        return list_value
    elif re.fullmatch("Да", user_word, flags=re.I):
        while True:
            print("Введите слово:")
            string_word_input = input()
            words_sorted_data = reading_transactions_in_str(list_value, string_word_input)
            if not words_sorted_data:
                print("Такой транзакции не существует!")
            else:
                return words_sorted_data
    return []


def main() -> list | str:
    ''' Функция сборки модулей '''

    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )

    file_number = input()
    file_data = user_file_input(file_number)
    if not file_data:
        return "Введите значение от 1 до 3!"
    else:
        status = True
        while status:
            print(
                """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
            )
            status_name = input()
            status_data = user_status_input(file_data, status_name)
            if not status_data:
                print(f"Статус операции {status_name} недоступен или не существует в списке!")
            else:
                print("Отсортировать операции по дате? Да/Нет")
                status = False

    sorted_ascending = input()
    sorted_data = sorted_file_input(status_data, sorted_ascending)
    if not sorted_data:
        return 'Введите "да" или "нет"!'
    else:
        print("Выводить только рублевые тразакции? Да/Нет")
    value_input = input()
    value_data = value_file_input(sorted_data, value_input)
    if not value_data:
        return 'Введите "да" или "нет"!'
    else:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    word_input = input()
    word_data = word_file_input(value_data, word_input)

    if word_data:
        print("Распечатываю итоговый список транзакций...")
        time.sleep(3)
        counter = transactions_avg(word_data)
        print(f"Всего банковских операций в выборке: {sum(counter.values())}")
        operation_list = []
        end_word_data = mask_account_card(get_date(word_data))

        for trns in end_word_data:
            if file_counter == 1:
                date = trns.get("date", "N/A")
                description = trns.get("description", "N/A")
                from_card = trns.get("from", "N/A")
                to_card = trns.get("to", "N/A")
                currency = trns.get("operationAmount", {}).get("amount", "N/A")
                code = trns.get("operationAmount", {}).get("currency", {}).get("code", "N/A")
                operation = f"\n{date} {description}\n{from_card} -> {to_card}\nСумма: {currency} {code}\n"
                operation_list.append(operation)

            elif file_counter in [2, 3]:
                date = trns.get("date", "N/A")
                description = trns.get("description", "N/A")
                from_card = trns.get("from", "N/A")
                to_card = trns.get("to", "N/A")
                currency = trns.get("amount", "N/A")
                code = trns.get("currency_code", "N/A")
                operation = f"\n{date} {description}\n{from_card} -> {to_card}\nСумма: {currency} {code}\n"
                operation_list.append(operation)

        return "".join(operation_list)
    return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"


if __name__ == "__main__":
    print(main())
