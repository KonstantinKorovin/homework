import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture()
def test_filter_state():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture()
def executed_state():
    return "EXECUTED"


@pytest.fixture()
def canceled_state():
    return "CANCELED"


def test_filter_executed(test_filter_state, executed_state):
    assert filter_by_state(test_filter_state, executed_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_canceled(test_filter_state, canceled_state):
    assert filter_by_state(test_filter_state, canceled_state) == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "list_dict_filter, state, expected",
    [
        (
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
            "EXECUTED",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], "CANCELED", []),
        (
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
            "ExEcUtEd",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
            "CANCELED",
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
        ),
        ([{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}], "EXECUTED", []),
        (
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
            "CaNcElEd",
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
        ),
    ],
)
def test_mark_parametrize_state(list_dict_filter, state, expected):
    assert filter_by_state(list_dict_filter, state) == expected


@pytest.fixture()
def test_sort_by_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture()
def true_sort_by_date():
    return True


@pytest.fixture()
def false_sort_by_date():
    return False


@pytest.fixture()
def only_one_sorted():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sorted_true(test_sort_by_date, true_sort_by_date):
    assert sort_by_date(test_sort_by_date, true_sort_by_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sorted_false(test_sort_by_date, false_sort_by_date):
    assert sort_by_date(test_sort_by_date, false_sort_by_date) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sorted_only_one_date(only_one_sorted, true_sort_by_date):
    assert sort_by_date(only_one_sorted, true_sort_by_date) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "data_sort_dict, date_sort, expected",
    [
        (
            [{"id": 1, "state": "Ex", "date": "2018-06-31.."}, {"id": 2, "state": "Ex", "date": "2018-07-30.."}],
            True,
            [{"id": 2, "state": "Ex", "date": "2018-07-30.."}, {"id": 1, "state": "Ex", "date": "2018-06-31.."}],
        ),
        (
            [{"id": 1, "state": "Ex", "date": "2018-06-31.."}, {"id": 2, "state": "Ex", "date": "2018-07-30.."}],
            False,
            [{"id": 1, "state": "Ex", "date": "2018-06-31.."}, {"id": 2, "state": "Ex", "date": "2018-07-30.."}],
        ),
    ],
)
def test_mark_sorted_date(data_sort_dict, date_sort, expected):
    assert sort_by_date(data_sort_dict, date_sort) == expected
