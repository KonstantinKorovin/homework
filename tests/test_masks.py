import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture()
def test_mask_number():
    return "1111222233334444"


@pytest.fixture()
def test_space_mask_number():
    return "1234123412341234"


def test_mask_card_number(test_mask_number):
    assert get_mask_card_number(test_mask_number) == "1111 22** **** 4444"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1111222233334444", "1111 22** **** 4444"),
        ("1234123412341234", "1234 12** **** 1234"),
        ("4321432143214321", "4321 43** **** 4321"),
    ],
)
def test_mask_card_number1(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_space_card_number(test_space_mask_number):
    assert get_mask_card_number(test_space_mask_number) == "1234 12** **** 1234"


@pytest.fixture()
def test_mask_account():
    return "11112222333344445555"


@pytest.fixture()
def test_space_mask_account():
    return "12341234123412341234"


def test_masked_account(test_mask_account):
    assert get_mask_account(test_mask_account) == "**5555"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("11112222333344445555", "**5555"),
        ("12341234123412341234", "**1234"),
        ("43214321432143214321", "**4321"),
    ],
)
def test_mask_account_card(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_space_card_mask(test_mask_account):
    assert get_mask_account(test_mask_account) == "**5555"
