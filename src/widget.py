from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name: str) -> str:
    """Функция маскирующая номер карты/счёта"""
    text_result = ""
    digit_result = ""
    digit_count = 0
    for el in name:
        if el.isalpha():
            text_result += el
        elif el.isdigit():
            digit_result += el
            digit_count += 1
    if digit_count == 20:
        return f"{text_result} {get_mask_account(digit_result)}"
    elif digit_count == 16:
        return f"{text_result} {get_mask_card_number(digit_result)}"
    return "Вы ввели неккоректную информацию"


def get_date(str_data: str) -> str:
    """Функция принимает строку и возвращает значение в формате ДД.ММ.ГГГГ"""
    if len(str_data) != 26:
        return "Введите сообщение в корректном формате"
    return f"{str_data[8:10]}.{str_data[5:7]}.{str_data[:4]}"
