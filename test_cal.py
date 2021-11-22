import pytest
from cal import addition, subtraction, multiplication

def test_addition():
    res = addition(2,5)
    if res == 7:
        assert True
    else:
        assert False


def test_multiplication():
    res = multiplication(3, 0)
    if res == 0:
        assert True
    else:
        assert False


def test_subtraction():
    res = subtraction(5, 2)
    if res == 3:
        assert True
    else:
        assert False
