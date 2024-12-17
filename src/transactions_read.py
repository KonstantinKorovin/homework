import pandas as pd

csv_df = pd.read_csv("/Users/krynik/PycharmProjects/bank_vidget/data/transactions.csv")


def reading_csv_transactions(csv_df: pd.DataFrame) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    csv_df_dict = csv_df.to_dict("records")
    return csv_df_dict


excel_df = pd.read_excel("/Users/krynik/PycharmProjects/bank_vidget/data/transactions_excel.xlsx")


def reading_excel_transactions(excel_df: pd.DataFrame) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""
    excel_df_dict = excel_df.to_dict("records")
    return excel_df_dict
