from typing import Generator, Iterable, Union

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(
    transactions: Iterable[dict], value: Union[str, None] = None
) -> Generator[Union[str, dict], None, None]:
    """Функция последовательно выдает транзакции где валюта соответсвует заданной"""
    if not value:
        yield "Валюта отсутствует"
    for transaction in transactions:
        filter_transactions = transaction["operationAmount"]["currency"]["code"]
        if filter_transactions == value:
            yield transaction


f = filter_by_currency(transactions, "RUB")
try:
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
except StopIteration:
    print("stop!")


def transaction_descriptions(transactions: Iterable[dict]) -> Generator[str]:
    """Функция последовательно выдает операции"""
    if not transactions:
        yield "Список отсутствует"
    else:
        for transaction in transactions:
            yield transaction["description"]


d = transaction_descriptions([])
try:
    print(next(d))
    print(next(d))
    print(next(d))
    print(next(d))
    print(next(d))
    print(next(d))
except StopIteration:
    print("stop!")


def card_number_generator(start: int | str, stop: int | str) -> Generator[str, None, None]:
    """Генератор номеров банковских карт в заданном диапазоне"""
    try:
        start_int = int(start)
        stop_int = int(stop)
    except ValueError:
        raise ValueError("Начальное и конечное значения должны быть числами или строками, представляющими числа")

    if not (0 <= start_int <= 9999999999999999 and 0 <= stop_int <= 9999999999999999):
        raise ValueError("Начальное и конечное значения должны быть в диапазоне от 0 до 9999999999999999")

    if start_int > stop_int:
        start_int, stop_int = stop_int, start_int

    for i in range(start_int + 1, stop_int + 1):
        card_number = str(i).zfill(16)  # Дополняем нулями слева до 16 цифр
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"


g = card_number_generator(0, 5)
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    print("stop!")
