import pytest

def add_numbers(a,b):
    return a + b


@pytest.mark.parametrize("a,b,expected" , [
    (1,2,3),
    (4,5,9),
    (11,2,13),
    (20,10,30),
    (23,7,30)
])


def test_add_numbers(a, b, expected):
    assert add_numbers(a,b) == expected