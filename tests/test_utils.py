import json
import os
import unittest
from unittest.mock import mock_open, patch

import pytest

from src.utils import load_transactions


@pytest.fixture
def test_load_transactions():
    return load_transactions("/Users/krynik/PycharmProjects/bank_vidget/data/operations.json")


def test_load_transactions1(test_load_transactions):
    assert (
        load_transactions("/Users/krynik/PycharmProjects/bank_vidget/data/operations.json") == test_load_transactions
    )


class TestLoadTransactions(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.abspath(os.path.dirname(__file__))
        self.data_dir = os.path.join(self.base_dir, "..", "data")
        self.file_path = os.path.join(self.data_dir, os.path.basename("operations.json"))

    def test_load_transactions_valid_json(self):
        test_data = [{"id": 1}, {"id": 2}]
        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
            transactions = load_transactions(self.file_path)
        self.assertEqual(transactions, test_data)

    def test_load_transactions_empty_json(self):
        with patch("builtins.open", mock_open(read_data=json.dumps([]))):
            transactions = load_transactions(self.file_path)
        self.assertEqual(transactions, [])

    def test_load_transactions_not_list_json(self):
        test_data = {"key": "value"}
        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
            transactions = load_transactions(self.file_path)
        self.assertEqual(transactions, [])

    def test_load_transactions_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            transactions = load_transactions(self.file_path)
        self.assertEqual(transactions, [])

    def test_load_transactions_json_decode_error(self):
        with patch("builtins.open", mock_open(read_data="invalid json")):
            transactions = load_transactions(self.file_path)
        self.assertEqual(transactions, [])
