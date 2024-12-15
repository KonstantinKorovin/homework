import datetime
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_transaction_amount(transaction: dict) -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float"""
    if transaction["operationAmount"]["currency"]["code"] in "RUB":
        return transaction["operationAmount"]["amount"]
    elif transaction["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
        api_key = os.getenv("API-KEY")
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&"
            f'from={transaction["operationAmount"]["currency"]["code"]}&'
            f'amount={transaction["operationAmount"]["amount"]}&date={datetime.datetime.now()}'
        )

        headers = api_key
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data["info"]["rate"]
            return float(transaction["operationAmount"]["amount"]) * float(exchange_rate)
        return []
    else:
        return []


print(
    get_transaction_amount(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    )
)
