from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions
import pytest

@pytest.fixture()
def test_no_value():
    return "Валюта отсутствует"


def test_no_value_filter(test_no_value):
    f = filter_by_currency(transactions, "")
    assert next(f) == test_no_value


def test_filter_usd():
    f = filter_by_currency(transactions, "USD")
    assert next(f) == {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
     "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
     "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702",}

    assert next(f) == {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
        "to":"Счет 75651667383060284188",}

    assert next(f) == {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",}

    with pytest.raises(StopIteration):
        assert next(f)


def test_filter_rub():
    z = filter_by_currency(transactions, "RUB")
    assert next(z) == {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",}

    assert next(z) == {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",}

    with pytest.raises(StopIteration):
        assert next(z)


@pytest.fixture()
def test_transaction1():
    return "Перевод организации"


def test_transactions1(test_transaction1):
    d = transaction_descriptions(transactions)
    assert next(d) == test_transaction1


@pytest.fixture()
def test_transaction2():
    return "Список отсутствует"


def test_transactions2(test_transaction2):
    d = transaction_descriptions([])
    assert next(d) == test_transaction2


@pytest.mark.parametrize("transactions, expected",
[([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации", "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"}], "Перевод организации"),

([{"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
   "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
   "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
   "to": "Счет 75651667383060284188"}], "Перевод со счета на счет"),

([{"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404",
   "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
   "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719",
   "to": "Счет 74489636417521191160"}], "Перевод со счета на счет"),

([{"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
   "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
   "description": "Перевод с карты на карту",
   "from": "Visa Classic 6831982476737658", "to": "Visa Platinum 8990922113665229"}], "Перевод с карты на карту"),

([{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
   "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
   "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
   "to": "Счет 14211924144426031657"}], "Перевод организации"),

([], "Список отсутсвует")])


def test_mark_transactions_parametrize(transactions, expected):
    d = transaction_descriptions(transactions) == expected


@pytest.fixture()
def test_card_number1():
    return "0000 0000 0000 0001"


def test_legit_card1(test_card_number1):
    n = card_number_generator(0,1)
    assert next(n) == test_card_number1


@pytest.fixture()
def test_card_number2():
    return "0000 0000 0000 0002"


def test_legit_card2(test_card_number2):
    n = card_number_generator(1,2)
    assert next(n) == test_card_number2


@pytest.mark.parametrize("start, stop, expected",
    [(2, 3, "0000 0000 0000 0003"),
     (1111111111111111, 1111111111111112, "1111 1111 1111 1112"),
     ([],[], "Начальное и конечное значения должны быть числами или строками, представляющими числа"),
     (-1, -3, "Начальное и конечное значения должны быть в диапазоне от 0 до 9999999999999999")])


def test_mark_card_number(start, stop, expected):
    m = card_number_generator(start, stop) == expected