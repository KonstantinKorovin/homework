import os
import unittest
from typing import Any
from unittest.mock import patch, MagicMock
from src.external_api import get_transaction_amount
import requests
from dotenv import load_dotenv

load_dotenv()


class TestGetTransactionAmount(unittest.TestCase):
    def setUp(self):
        self.api_key = "test_api_key"  # Set a test API key
        os.environ["API-KEY"] = self.api_key  # Set the environment variable

    def tearDown(self):
        os.environ.pop("API-KEY", None)  # remove API-KEY for not affecting the other tests

    def test_get_transaction_amount_rub(self):
        transaction = {"currency": "RUB", "amount": 100}
        amount = get_transaction_amount(transaction)
        self.assertEqual(amount, 100)

    @patch("requests.get")
    def test_get_transaction_amount_usd(self, mock_get):
        transaction = {"currency": "USD", "amount": 10}
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"RUB": 90.0}}
        mock_get.return_value = mock_response
        amount = get_transaction_amount(transaction)
        self.assertEqual(amount, 900.0)
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_get_transaction_amount_eur(self, mock_get):
        transaction = {"currency": "EUR", "amount": 5}
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"RUB": 100.0}}
        mock_get.return_value = mock_response
        amount = get_transaction_amount(transaction)
        self.assertEqual(amount, 500.0)
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_get_transaction_amount_usd_api_error(self, mock_get):
        transaction = {"currency": "USD", "amount": 10}
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response
        amount = get_transaction_amount(transaction)
        self.assertIsNone(amount)
        mock_get.assert_called_once()

    def test_get_transaction_amount_unknown_currency(self):
        transaction = {"currency": "GBP", "amount": 100}
        amount = get_transaction_amount(transaction)
        self.assertIsNone(amount)

    @patch("requests.get")
    def test_get_transaction_amount_no_api_key(self, mock_get):
        os.environ.pop("API-KEY")
        transaction = {"currency": "USD", "amount": 10}
        amount = get_transaction_amount(transaction)
        self.assertIsNone(amount)