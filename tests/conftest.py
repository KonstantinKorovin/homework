import pytest


# Фикстуры для decorators.py
@pytest.fixture
def test_decorator_first():
    return "my_function ok\n3\n"


@pytest.fixture
def test_decorator_second():
    return "my_function ok\n1\n"


@pytest.fixture
def test_decorator_third():
    return "my_function error: unsupported operand " "type(s) for +: 'int' and 'str'. Inputs: (1, ''), {}\n"


@pytest.fixture
def test_decorator_four():
    return "my_function error: unsupported operand " "type(s) for +: 'int' and 'list'. Inputs: (1, [1]), {}\n"


# Фикстуры для generators.py
@pytest.fixture
def transactions_json():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


@pytest.fixture()
def test_name_transaction_first():
    return "Перевод организации"


@pytest.fixture()
def test_name_transaction_second():
    return "Перевод с карты на карту"


@pytest.fixture()
def transactions_csv_and_xlsx():
    return [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "rub",
            "currency_code": "RUB",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "dol",
            "currency_code": "USD",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "dall",
            "currency_code": "USD",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.fixture()
def test_card_number1():
    return "0000 0000 0000 0001"


@pytest.fixture()
def test_card_number2():
    return "0000 0000 0000 0002"


# Фикстуры для masks.py
@pytest.fixture()
def test_mask_number():
    return "1111 22** **** 4444"


@pytest.fixture()
def test_mask_account():
    return "11112222333344445555"


# Фикстуры для transactions_read.py
@pytest.fixture()
def fixture_csv():
    return {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }


@pytest.fixture()
def fixture_csv1():
    return {
        "id": "4699552",
        "state": "EXECUTED",
        "date": "2022-03-23T08:29:37Z",
        "amount": "23423",
        "currency_name": "Peso",
        "currency_code": "PHP",
        "from": "Discover 7269000803370165",
        "to": "American Express 1963030970727681",
        "description": "Перевод с карты на карту",
    }


@pytest.fixture()
def fixture_excel():
    return {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }


@pytest.fixture()
def fixture_excel1():
    return {
        "id": 4699552.0,
        "state": "EXECUTED",
        "date": "2022-03-23T08:29:37Z",
        "amount": 23423.0,
        "currency_name": "Peso",
        "currency_code": "PHP",
        "from": "Discover 7269000803370165",
        "to": "American Express 1963030970727681",
        "description": "Перевод с карты на карту",
    }


@pytest.fixture()
def list_transactions_fixture():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 214024827,
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
            "operationAmount": {"amount": "70946.18", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366",
        },
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {"amount": "51463.70", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "to": "Счет 38976430693692818358",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.fixture()
def dict_transactions():
    return [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        }
    ]
