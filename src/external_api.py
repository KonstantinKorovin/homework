import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_transaction_amount(transaction: dict) -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float"""
    if transaction["currency"] == "RUB":
        return transaction["amount"]
    elif transaction["currency"] in ["USD", "EUR"]:
        api_key = os.getenv("API-KEY")
        url = (
            f"https://api.apilayer.com/exchangerates_data/latest?"
            f'base={transaction["currency"]}&symbols=RUB&apikey={api_key}'
        )
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data["rates"]["RUB"]
            return float(transaction["amount"]) * float(exchange_rate)
        else:
            return []
    else:
        return []
