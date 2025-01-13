from typing import Generator, Iterable, Union, Iterator


def filter_by_currency(
    transactions: Iterable[dict], value: Union[str, None] = None, table_mode: bool = False
) -> Generator[Union[str, dict], None, None]:
    """Функция последовательно выдает транзакции где валюта соответсвует заданной"""
    if not value:
        yield "Валюта отсутствует"
    for transaction in transactions:
        if table_mode:
            currency_code = transaction.get("currency_code", "Nan val")
        else:
            currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if currency_code == value:
            yield transaction


def transaction_descriptions(transactions: Iterable[dict]) -> Iterator[str]:
    """Функция последовательно выдает операции"""
    for transaction in transactions:
        yield transaction.get("description", "Список отсутствует")


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
