from main import PATH_TO_CSV, PATH_TO_XLSX
from src.transactions_read import (reading_csv_transactions, reading_excel_transactions, reading_transactions_in_str,
                                   transactions_avg)


def test_fixture_csv(fixture_csv):
    assert reading_csv_transactions(PATH_TO_CSV)[0] == fixture_csv


def test_fixture_csv1(fixture_csv1):
    assert reading_csv_transactions(PATH_TO_CSV)[-1] == fixture_csv1


def test_fixture_excel(fixture_excel):
    assert reading_excel_transactions(PATH_TO_XLSX)[0] == fixture_excel


def test_fixture_excel1(fixture_excel1):
    assert reading_excel_transactions(PATH_TO_XLSX)[-1] == fixture_excel1


def test_transactions_list(list_transactions_fixture, dict_transactions):
    assert reading_transactions_in_str(list_transactions_fixture, "Открытие вклада") == dict_transactions


def test_transactions_avg(list_transactions_fixture):
    assert transactions_avg(list_transactions_fixture) == {
        "Открытие вклада": 1,
        "Перевод организации": 5,
        "Перевод с карты на карту": 1,
        "Перевод со счета на счет": 2,
    }
