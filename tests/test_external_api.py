import unittest
import os
from dotenv import load_dotenv
from unittest.mock import patch, MagicMock
from src.external_api import get_transaction_amount
class TestGetTransactionAmount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Загрузка переменных окружения
        load_dotenv()
        cls.api_key = os.getenv("API-KEY")

    @patch('requests.get')
    def test_transaction_in_rub(self, mock_get):
        # Тест для транзакции в рублях
        transaction = {"currency": "RUB", "amount": 1000}
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"rates": {"RUB": 1.0}})
        self.assertEqual(get_transaction_amount(transaction), 1000.0)

    @patch('requests.get')
    def test_transaction_in_usd(self, mock_get):
        # Тест для транзакции в долларах
        transaction = {"currency": "USD", "amount": 100}
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"rates": {"RUB": 75.0}})
        self.assertEqual(get_transaction_amount(transaction), 7500.0)

    @patch('requests.get')
    def test_transaction_in_eur(self, mock_get):
        # Тест для транзакции в евро
        transaction = {"currency": "EUR", "amount": 50}
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"rates": {"RUB": 80.0}})
        self.assertEqual(get_transaction_amount(transaction), 4000.0)

    def test_transaction_unsupported_currency(self):
        # Тест для транзакции с неподдерживаемой валютой
        transaction = {"currency": "GBP", "amount": 100}
        self.assertEqual(get_transaction_amount(transaction), [])

    @patch('requests.get')
    def test_api_request_failure(self, mock_get):
        # Тест для случая, когда API запрос неудачен
        transaction = {"currency": "USD", "amount": 100}
        mock_get.return_value = MagicMock(status_code=400)
        self.assertEqual(get_transaction_amount(transaction), [])
