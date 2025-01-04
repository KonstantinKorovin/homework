import csv
import re
from collections import Counter

import pandas as pd

csv_df = "/Users/krynik/PycharmProjects/bank_vidget/data/transactions.csv"


def reading_csv_transactions(filename_csv: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    with open(csv_df, "r", newline="") as file:
        csv_df_dict = csv.DictReader(file, delimiter=";")
        return list(csv_df_dict)


excel_df = pd.read_excel("/Users/krynik/PycharmProjects/bank_vidget/data/transactions_excel.xlsx")


def reading_excel_transactions(filename_excel: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""
    excel_df_dict = excel_df.to_dict("records")
    return excel_df_dict


filename_json = "/Users/krynik/PycharmProjects/bank_vidget/data/operations.json"


def reading_transactions_in_str(file_transactions_: list, string_search: str) -> list:
    """Функция для поиска банковских операций в списке по заданной строке"""
    string = string_search.replace(" ", "")
    new_transactions_list = [
        trns
        for trns in file_transactions_
        if re.fullmatch(string, str(trns.get("description", "Неизвестная операция")).replace(" ", ""), flags=re.I)
    ]

    return new_transactions_list


def transactions_avg(file_transactions: list) -> dict:
    """Функция для подсчета количества банковских операций определенного типа"""
    new_operations = [operation.get("description", "Неизвестная операция") for operation in file_transactions]
    return Counter(new_operations)
