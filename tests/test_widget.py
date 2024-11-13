from src.widget import mask_account_card, get_date
import pytest


@pytest.fixture()
def test_mask_account():
    return "12345678901234567890"


@pytest.fixture()
def test_mask_card():
    return "1234567890123456"


def test_mask_bank_account(test_mask_account):
    assert mask_account_card(test_mask_account) == " **7890"


def test_mask_bank_number(test_mask_card):
    assert mask_account_card(test_mask_card) == " 1234 56** **** 3456"


@pytest.mark.parametrize("name, expected", [("Visa Platinum 1234 1234 1234 1234", "VisaPlatinum 1234 12** **** 1234"),
                                            ("VisaPlatinum1231123112311231", "VisaPlatinum 1231 12** **** 1231"),
                                            ("Maestro12311231123112312", "Вы ввели неккоректную информацию"),
                                            ("Maestro123112311231123", "Вы ввели неккоректную информацию"),
                                            ("Счет 1234 1234 1234 1234 1234", "Счет **1234"),
                                            ("Счет12311231123112311231", "Счет **1231"),
                                            ("Счет 1234 1234 1234 1234 12345", "Вы ввели неккоректную информацию"),
                                            ("Счет 1234 1234 1234 1234 123", "Вы ввели неккоректную информацию"),])


def test_mark_mask_account_card(name, expected):
    assert mask_account_card(name) == expected

    with pytest.raises(TypeError):
        assert mask_account_card(12345)

    with pytest.raises(TypeError):
        assert mask_account_card()


@pytest.fixture()
def test_get_date():
    return "2024-03-11T02:26:18.671407"


def tested_get_dates(test_get_date):
    assert  get_date(test_get_date) == "11.03.2024"


@pytest.mark.parametrize("str_data, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                                ("2012-10-31............wq.w", "31.10.2012"),
                                                ("2024-03-11T02:26:18.6714071", "Введите сообщение в корректном формате"),
                                                ("2024-03-11T02:26:18.67140", "Введите сообщение в корректном формате")])

def test_mark_data(str_data, expected):
    assert get_date(str_data) == expected

    with pytest.raises(TypeError):
        assert get_date(12345)

    with pytest.raises(TypeError):
        assert get_date()