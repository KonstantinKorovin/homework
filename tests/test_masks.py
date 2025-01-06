import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(test_mask_number):
    assert get_mask_card_number("1111222233334444") == test_mask_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("0000000000000000", "0000 00** **** 0000"),
        ("1234 1234 1234 1234", "Неверный формат номера карты"),
        ("[]", "Неверный формат номера карты"),
    ],
)
def test_mask_card_number1(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_masked_account(test_mask_account):
    assert get_mask_account(test_mask_account) == "**5555"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1111 2222 3333 4444 5555", "Неверный формат номера счета"),
        ("{}", "Неверный формат номера счета"),
        ("43214321432143214321", "**4321"),
    ],
)
def test_mask_account_card(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_space_card_mask(test_mask_account):
    assert get_mask_account(test_mask_account) == "**5555"
