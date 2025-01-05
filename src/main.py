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
data_dir = os.path.join(os.path.dirname(src_dir), "data")

# Получаем пути к файлам
PATH_TO_JSON = os.path.join(data_dir, "operations.json")
PATH_TO_CSV = os.path.join(data_dir, "transactions.csv")
PATH_TO_XLSX = os.path.join(data_dir, "transactions_excel.xlsx")


def main() -> str:
    """Основная логика программы"""
    file_counter = 0

    def user_file_format() -> list:
        """Функция выборки файла пользователем"""
        nonlocal file_counter
        while True:
            print(
                """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
            )

            user_file_input = input()
            if user_file_input == "1":
                print("Для обработки выбран JSON-файл")
                file_counter = 1
                return load_transactions(PATH_TO_JSON)
            elif user_file_input == "2":
                print("Для обработки выбран CSV-файл")
                file_counter = 2
                return reading_csv_transactions(PATH_TO_CSV)
            elif user_file_input == "3":
                print("Для обработки выбран XLSX-файл")
                file_counter = 3
                return reading_excel_transactions(PATH_TO_XLSX)
            else:
                print("Введите значение от 1 до 3!")

    def status_user_filter(filename_list: list) -> list:
        """Функция выборки статуса по которому будет происходить фильтрация файла"""
        while True:
            print(
                """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
            )

            status_input = input()
            if status_input.upper().replace(" ", "") == "EXECUTED":
                print("Операции отфильтрованы по статусу 'EXECUTED'")
                return filter_by_state(filename_list, "EXECUTED")
            elif status_input.upper().replace(" ", "") == "CANCELED":
                print("Операции отфильтрованы по статусу 'CANCELED'")
                return filter_by_state(filename_list, "CANCELED")
            elif status_input.upper().replace(" ", "") == "PENDING":
                print("Операции отфильтрованы по статусу 'PENDING'")
                return filter_by_state(filename_list, "PENDING")
            else:
                print(f"Статус операции {status_input} недоступен!")

    def sorted_date_user(filtered_list: list) -> list:
        """Функция сортировки списка по дате"""
        while True:
            print("Отсортировать операции по дате? Да/Нет")
            sorted_list_input = input()
            if re.fullmatch("Нет", sorted_list_input, flags=re.I):
                return filtered_list
            elif re.fullmatch("Да", sorted_list_input, flags=re.I):
                break
            else:
                print("Введите 'Да' или 'Нет'!")
        while True:
            print("Отсортировать по возрастанию или по убыванию?")
            from_sorted_list_input = str(input())
            if re.fullmatch("по возрастанию", from_sorted_list_input, flags=re.I):
                return sort_by_date(filtered_list, False)
            elif re.fullmatch("по убыванию", from_sorted_list_input, flags=re.I):
                return sort_by_date(filtered_list, True)
            else:
                print("Введите 'по возрастанию' или 'по убыванию'!")

    def transaction_filtered_in_value(sorted_list: list) -> list:
        """Функция выдает список рублевых транзакций если пользователь явно указывает на это"""
        while True:
            print("Выводить только рублевые тразакции? Да/Нет")
            filter_rub_input = input()
            if re.fullmatch("Нет", filter_rub_input, flags=re.I):
                return sorted_list
            elif re.fullmatch("Да", filter_rub_input, flags=re.I) and (file_counter == 2 or file_counter == 3):
                return list(filter_by_currency(sorted_list, "RUB", True))
            elif re.fullmatch("Да", filter_rub_input, flags=re.I) and file_counter == 1:
                return list(filter_by_currency(sorted_list, "RUB"))
            else:
                print("Введите 'Да' или 'Нет'!")

    def transaction_filtered_in_words(transaction_sorted_value: list) -> list:
        """функция фильтрации транзакций по определенному слову"""
        while True:
            print("""Отфильтровать список транзакций по определенному слову в описании? Да/Нет""")
            words_filtered_input = input()
            if re.fullmatch("Нет", words_filtered_input, flags=re.I):
                print("Распечатываю итоговый список транзакций...")
                time.sleep(3)
                print(f"Всего банковских операций в выборке: {len(transaction_sorted_value)}")
                return transaction_sorted_value
            elif re.fullmatch("Да", words_filtered_input, flags=re.I):
                break
            else:
                print("Введите 'Да' или 'Нет'!")
        while True:
            print("Введите название операции:")
            operation_input = input().capitalize()

            filtered_transactions = reading_transactions_in_str(transaction_sorted_value, operation_input)

            if filtered_transactions:
                print("Распечатываю итоговый список транзакций...")
                time.sleep(3)
                counter = transactions_avg(filtered_transactions)
                print(f"Всего банковских операций в выборке: {counter[operation_input]}")
                return filtered_transactions
            else:
                print(f"Операций с названием: '{operation_input}' не сществует. Введите корректное название операции!")

    full_data = mask_account_card(
        get_date(
            transaction_filtered_in_words(
                transaction_filtered_in_value(sorted_date_user(status_user_filter(user_file_format())))
            )
        )
    )

    operations_list = []

    for data in full_data:
        if not full_data:
            return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
        elif full_data and (file_counter == 2 or file_counter == 3):
            date_str = data.get("date")
            description_str = data.get("description")
            from_str = data.get("from", "N/A")
            to_str = data.get("to", "N/A")
            amount_str = data.get("amount")
            currency_code_str = data.get("currency_code")

            operation = (
                f"\n{date_str} {description_str} \n{from_str} -> {to_str} \nСумма: {amount_str} {currency_code_str}\n"
            )

            operations_list.append(operation)

        elif full_data and file_counter == 1:
            date_str = data.get("date")
            description_str = data.get("description")
            from_str = data.get("from", "N/A")
            to_str = data.get("to", "N/A")
            amount_str = data.get("operationAmount", {}).get("amount")
            currency_code_str = data.get("operationAmount", {}).get("currency", {}).get("code")

            operation = (
                f"\n{date_str} {description_str} \n{from_str} -> {to_str} \nСумма: {amount_str} {currency_code_str}\n"
            )

            operations_list.append(operation)
    return "".join(operations_list)


if __name__ == "__main__":
    print(main())
