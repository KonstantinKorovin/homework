import logging
from typing import Any

masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler("/Users/krynik/PycharmProjects/bank_vidget/logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Any = str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    masks_logger.info("Starting app..")
    masks_logger.info("Initialization card_number..")
    if len(card_number) != 16:
        masks_logger.error("Error format card number!")
        masks_logger.info("Finished app")
        return "Неверный формат номера карты"
    else:
        masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        masks_logger.info("Success!")
        masks_logger.info("Finished app")
        return masked_card_number


def get_mask_account(account_number: Any = str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    masks_logger.info("Starting app..")
    masks_logger.info("Initialization account..")
    if len(account_number) != 20:
        masks_logger.error("Error format mask!")
        masks_logger.info("Finished app")
        return "Неверный формат номера счета"
    else:
        masked_account_number = f"**{account_number[-4:]}"
        masks_logger.info("Success!")
        masks_logger.info("Finished app")
        return masked_account_number
