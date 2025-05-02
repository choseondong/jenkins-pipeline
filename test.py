import pytest

def add(num1,num2):
    return num1 - num2

def test_add_positive_numbers():
    assert add(2,3) == 5, "2+3 은 5"