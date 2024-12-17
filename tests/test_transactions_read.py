from unittest.mock import Mock

import pytest

from src.transactions_read import csv_df, excel_df, reading_csv_transactions, reading_excel_transactions


@pytest.fixture()
def fixture_csv():
    return {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }


def test_fixture_csv(fixture_csv):
    assert reading_csv_transactions(csv_df)[0] == fixture_csv


@pytest.fixture()
def fixture_csv1():
    return {
        "id": "4699552",
        "state": "EXECUTED",
        "date": "2022-03-23T08:29:37Z",
        "amount": "23423",
        "currency_name": "Peso",
        "currency_code": "PHP",
        "from": "Discover 7269000803370165",
        "to": "American Express 1963030970727681",
        "description": "Перевод с карты на карту",
    }


def test_fixture_csv1(fixture_csv1):
    assert reading_csv_transactions(csv_df)[-1] == fixture_csv1


@pytest.fixture()
def fixture_excel():
    return {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }


def test_fixture_excel(fixture_excel):
    assert reading_excel_transactions(excel_df)[0] == fixture_excel


@pytest.fixture()
def fixture_excel1():
    return {
        "id": 4699552.0,
        "state": "EXECUTED",
        "date": "2022-03-23T08:29:37Z",
        "amount": 23423.0,
        "currency_name": "Peso",
        "currency_code": "PHP",
        "from": "Discover 7269000803370165",
        "to": "American Express 1963030970727681",
        "description": "Перевод с карты на карту",
    }


def test_fixture_excel1(fixture_excel1):
    assert reading_excel_transactions(excel_df)[-1] == fixture_excel1


def test_reading_csv_transactions():
    mock_random = Mock(return_value=5)
    reading_csv_transactions = mock_random
    assert reading_csv_transactions() == 5
    mock_random.assert_called_once()


def test_reading_excel_transactions():
    mock_random = Mock(return_value=5)
    reading_excel_transactions = mock_random
    assert reading_excel_transactions() == 5
    mock_random.assert_called_once()
