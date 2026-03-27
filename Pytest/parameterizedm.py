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

@pytest.mark.add
def test_add_numbers(a, b, expected):
    assert add_numbers(a,b) == expected


def subtract(a,b):
    return a-b


@pytest.mark.parametrize("a,b,expected" , [
    (5,2,3),
    (6,2,4),
    (18,6,6),
    (15,5,10),
])

@pytest.mark.subtract
def test_subtractNumber(a,b,expected):
    assert subtract(a,b) == expected