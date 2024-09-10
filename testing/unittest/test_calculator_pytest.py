# test_calculator.py
from calculator import add


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# To run this code : pytest unittest/test_calculator_pytest.py
