import csv
import re
from collections import Counter

import pandas as pd


def reading_csv_transactions(filename_csv: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    with open(filename_csv, "r", encoding="utf-8", newline="") as file:
        csv_df_dict = csv.DictReader(file, delimiter=";")
        return list(csv_df_dict)


def reading_excel_transactions(filename_excel: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""
    excel_df_dict = pd.read_excel(filename_excel).to_dict("records")
    return excel_df_dict


def reading_transactions_in_str(file_transactions: list, string_search: str) -> list:
    """Функция для поиска банковских операций в списке по заданной строке"""
    pattern = re.compile(string_search)
    new_transactions_list = [
        transaction
        for transaction in file_transactions
        if "description" in transaction and pattern.search(transaction["description"])
    ]

    return new_transactions_list


def transactions_avg(file_transactions: list) -> dict:
    """Функция для подсчета количества банковских операций определенного типа"""
    new_operations = [operation.get("description", "Неизвестная операция") for operation in file_transactions]
    return Counter(new_operations)
