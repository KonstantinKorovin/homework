import pytest

from src.decorators import my_function


def test_my_function1(capsys):
    print(my_function(1, 2))
    captured = capsys.readouterr()
    assert captured.out == 'my_function ok\n3\n'


def test_my_function2(capsys):
    print(my_function(1, 0))
    captured = capsys.readouterr()
    assert captured.out == 'my_function ok\n1\n'


def test_my_function3(capsys):
    print(my_function(1, ''))
    captured = capsys.readouterr()
    assert captured.out == ('my_function error: unsupported operand type(s) for +: \'int\' and \'str\'. Inputs: (1, \'\'), {}\n')


def test_my_function4(capsys):
    print(my_function(1, [1]))
    captured = capsys.readouterr()
    assert captured.out == ('my_function error: unsupported operand type(s) for +: \'int\' and \'list\'. Inputs: (1, [1]), {}\n')