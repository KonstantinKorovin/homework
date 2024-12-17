import datetime
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def get_transaction_amount(transaction: dict) -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float"""
    date_now = datetime.datetime.now()
    date_string = date_now.strftime("%Y-%m-%d")
    if (
        transaction["operationAmount"]["currency"]["code"] in "USD"
        or transaction["operationAmount"]["currency"]["code"] in "EUR"
    ):
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}"
            f"&from={transaction['operationAmount']['currency']['code']}"
            f"&amount={transaction['operationAmount']['amount']}&date={date_string}"
        )

        headers = {"apikey": api_key}

        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            result = response.text
            return result
    elif transaction["operationAmount"]["currency"]["code"] in "RUB":
        return f"{float(transaction['operationAmount']['amount'])} RUB"
    else:
        return []
