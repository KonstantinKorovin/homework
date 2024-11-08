def filter_by_state(list_dict_filter: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""

    clean_dict = []

    for key in list_dict_filter:
        if key.get("state") == state:
            clean_dict.append(key)
    return clean_dict


def sort_by_date(data_sort_dict: list[dict], date_sort: bool = True) -> list[dict]:
    """Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате"""

    sorted_data = []

    if data_sort_dict:
        sorted_data = sorted(data_sort_dict, key=lambda x: x.get("date"), reverse=date_sort)
    return sorted_data
