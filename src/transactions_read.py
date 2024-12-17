import csv

import pandas as pd

csv_df = "/Users/krynik/PycharmProjects/bank_vidget/data/transactions.csv"


def reading_csv_transactions(filename_csv: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    with open(csv_df, "r", newline="") as file:
        csv_df_dict = csv.DictReader(file, delimiter=";")
        return list(csv_df_dict)


excel_df = pd.read_excel("/Users/krynik/PycharmProjects/bank_vidget/data/transactions_excel.xlsx")


def reading_excel_transactions(filename_excel: pd.DataFrame) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""
    excel_df_dict = excel_df.to_dict("records")
    return excel_df_dict
