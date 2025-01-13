import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(list_transactions: list) -> list:
    """Функция маскирующая номер карты/счёта"""
    for trns in list_transactions:
        trns_from = trns.get("from", "")
        trns_to = trns.get("to", "")
        if trns_from:
            pattern1 = re.findall(r"\d", str(trns_from))
            pattern2 = re.findall("([a-z]|[а-я])", str(trns_from), flags=re.I)

            if len(pattern1) == 16:
                trns["from"] = f"{''.join(pattern2)} {get_mask_card_number(''.join(pattern1))}"
            elif len(pattern1) == 20:
                trns["from"] = f"{''.join(pattern2)} {get_mask_account(''.join(pattern1))}"

        if trns_to:
            pattern3 = re.findall(r"\d", str(trns_to))
            pattern4 = re.findall("([a-z]|[а-я])", str(trns_to), flags=re.I)
            if len(pattern3) == 16:
                trns["to"] = f"{''.join(pattern4)} {get_mask_card_number(''.join(pattern3))}"
            elif len(pattern3) == 20:
                trns["to"] = f"{''.join(pattern4)} {get_mask_account(''.join(pattern3))}"

    return list_transactions


def get_date(str_data: list) -> list:
    """Функция принимает строку и возвращает значение в формате ДД.ММ.ГГГГ"""
    pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
    for data in str_data:
        match = pattern.search(data.get("date", "Неизвестная дата"))

        if match:
            if pattern.pattern == r"(\d{4})-(\d{2})-(\d{2})":
                data["date"] = f"{match.group(3)}.{match.group(2)}.{match.group(1)}"
    return str_data
