import datetime
import os
import unittest
from unittest.mock import MagicMock, patch

import requests
from dotenv import load_dotenv

load_dotenv()


class TestGetTransactionAmount(unittest.TestCase):
    def setUp(self):
        self.api_key = os.getenv("API-KEY")

    def get_transaction_amount(self, transaction: dict) -> float | list:
        """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float"""
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return float(transaction["operationAmount"]["amount"])
        elif transaction["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
            url = (
                f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&"
                f'from={transaction["operationAmount"]["currency"]["code"]}&'
                f'amount={transaction["operationAmount"]["amount"]}&date={datetime.datetime.now()}'
            )

            headers = {"apikey": self.api_key}
            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                exchange_rate = data["info"]["rate"]
                return float(transaction["operationAmount"]["amount"]) * float(exchange_rate)
            return []
        else:
            return []

    def test_get_transaction_amount_rub(self):
        transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "RUB"},
            }
        }
        self.assertEqual(self.get_transaction_amount(transaction), 100.00)

    @patch("requests.request")
    def test_get_transaction_amount_usd_success(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"info": {"rate": 75.0}}
        mock_request.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "USD"},
            }
        }

        expected_amount = 100.00 * 75.0
        actual_amount = self.get_transaction_amount(transaction)

        self.assertEqual(actual_amount, expected_amount)

    @patch("requests.request")
    def test_get_transaction_amount_eur_success(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"info": {"rate": 80.0}}
        mock_request.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": "50.00",
                "currency": {"code": "EUR"},
            }
        }

        expected_amount = 50.00 * 80.0
        actual_amount = self.get_transaction_amount(transaction)
        self.assertEqual(actual_amount, expected_amount)

    @patch("requests.request")
    def test_get_transaction_amount_usd_api_error(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_request.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "USD"},
            }
        }
        self.assertEqual(self.get_transaction_amount(transaction), [])

    def test_get_transaction_amount_unknown_currency(self):
        transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "GBP"},
            }
        }
        self.assertEqual(self.get_transaction_amount(transaction), [])
