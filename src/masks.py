from typing import Any


def get_mask_card_number(card_number: Any = str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    if len(card_number) != 16:
        return "Неверный формат номера карты"
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_card_number


def get_mask_account(account_number: Any = str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    if len(account_number) != 20:
        return "Неверный формат номера счета"
    masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number
