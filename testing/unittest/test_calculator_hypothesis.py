# test_calculator_hypothesis.py
from calculator import add
from hypothesis import given
import hypothesis.strategies as st


@given(st.integers(), st.integers())
def test_add(a, b):
    # valid
    assert add(a, b) == a + b
    # no valid
    assert add(a, b) != a - b


# to run pytest test_calculator_hypothesis.py
# pip install hypothesis
