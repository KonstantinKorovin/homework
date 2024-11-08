def filter_by_state(arg: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""

    dict_keys = []

    for key in arg:
        if key.get("state") == state:
            dict_keys.append(key)
    return dict_keys


def sort_by_date(dicts: list[dict], rev: str = "True") -> list[dict]:
    """Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате"""

    sorted_data = []

    if dicts:
        sorted_data = sorted(dicts, key=lambda x: x.get("date"), reverse=rev)
    return sorted_data
