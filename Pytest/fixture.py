import pytest
import math

@pytest.fixture
def setup_teardown():
    print("\nSetup: Connect to DB")
    
    yield  # 👉 test runs here
    
    print("\nTeardown: Close DB")


def test_case(setup_teardown):
    print("Running test")
    assert True





@pytest.fixture
def numbers():
    return [1, 2, 3]

@pytest.mark.will
def test_sum(numbers):
    assert sum(numbers) == 6

@pytest.mark.will
def test_max(numbers):
    assert max(numbers) == 3


@pytest.fixture
def provider():
    return [2,3,4,5,6]


def test_multiply(provider):
    result =  math.prod(provider)
    print(result)
    assert result == 720