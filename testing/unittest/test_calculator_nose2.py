from calculator import add


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(4, 0) == 0

# pip install nose2
# to run: nose2
