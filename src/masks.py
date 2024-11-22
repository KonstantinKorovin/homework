from typing import Any


def get_mask_card_number(card_number: Any = str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_numbers = card_number.replace(" ", "")
    if len(card_numbers) != 16 or card_numbers.isspace():
        return "Вы ввели неверный формат номера карты"
    else:
        masked_card_number = f"{card_numbers[:4]} {card_numbers[4:6]}** **** {card_numbers[12:]}"
        return masked_card_number


def get_mask_account(account_number: Any = str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    account_numbers = account_number.replace(" ", "")
    if len(account_numbers) != 20 or account_numbers.isspace():
        return "Вы ввели неверный формат номера счета"
    else:
        masked_account_number = f"**{account_number[-4:]}"
        return masked_account_number
