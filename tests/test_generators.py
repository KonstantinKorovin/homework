import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_json_transactions_usd(transactions_json):
    f = filter_by_currency(transactions_json, "USD", False)
    assert next(f) == transactions_json[1]
    assert next(f) == transactions_json[2]

    with pytest.raises(StopIteration):
        assert next(f)


def test_json_transactions_rub(transactions_json):
    z = filter_by_currency(transactions_json, "RUB", False)
    assert next(z) == transactions_json[0]

    with pytest.raises(StopIteration):
        assert next(z)


def test_csv_and_xlsx_transactions_usd(transactions_csv_and_xlsx):
    f = filter_by_currency(transactions_csv_and_xlsx, "USD", True)
    assert next(f) == transactions_csv_and_xlsx[1]
    assert next(f) == transactions_csv_and_xlsx[2]

    with pytest.raises(StopIteration):
        assert next(f)


def test_csv_and_xlsx_transactions_rub(transactions_csv_and_xlsx):
    z = filter_by_currency(transactions_csv_and_xlsx, "RUB", True)
    assert next(z) == transactions_csv_and_xlsx[0]

    with pytest.raises(StopIteration):
        assert next(z)


def test_transactions_json(test_name_transaction_first, transactions_json):
    d = transaction_descriptions(transactions_json)
    assert next(d) == test_name_transaction_first
    assert next(d) == test_name_transaction_first
    assert next(d) == test_name_transaction_first

    with pytest.raises(StopIteration):
        assert next(d)


def test_transactions_csv_and_xlsx(
    test_name_transaction_first, test_name_transaction_second, transactions_csv_and_xlsx
):
    b = transaction_descriptions(transactions_csv_and_xlsx)
    assert next(b) == test_name_transaction_first
    assert next(b) == test_name_transaction_second
    assert next(b) == test_name_transaction_second

    with pytest.raises(StopIteration):
        assert next(b)


def test__not_transactions():
    v = transaction_descriptions([])

    with pytest.raises(StopIteration):
        assert next(v)


def test_legit_card1(test_card_number1, test_card_number2):
    n = card_number_generator(0, 2)
    assert next(n) == test_card_number1
    assert next(n) == test_card_number2

    with pytest.raises(StopIteration):
        assert next(n)


def test_value_error_card_first():
    a = card_number_generator("", 2)
    with pytest.raises(ValueError):
        assert next(a)


def test_value_error_card_second():
    a = card_number_generator(-1, -3)
    with pytest.raises(ValueError):
        assert next(a)
