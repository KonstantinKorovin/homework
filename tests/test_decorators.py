from src.decorators import my_function


def test_my_function1(capsys, test_decorator_first):
    print(my_function(1, 2))
    captured = capsys.readouterr()
    assert captured.out == test_decorator_first


def test_my_function2(capsys, test_decorator_second):
    print(my_function(1, 0))
    captured = capsys.readouterr()
    assert captured.out == test_decorator_second


def test_my_function3(capsys, test_decorator_third):
    print(my_function(1, ""))
    captured = capsys.readouterr()
    assert captured.out == test_decorator_third


def test_my_function4(capsys, test_decorator_four):
    print(my_function(1, [1]))
    captured = capsys.readouterr()
    assert captured.out == test_decorator_four
