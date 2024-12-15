import pandas as pd
import openpyxl


cdf = pd.read_csv('/Users/krynik/PycharmProjects/bank_vidget/data/transactions.csv')


def reading_csv_transactions(cdf):
    ''' Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями '''
    return cdf
print(reading_csv_transactions(cdf))