import pytest

@pytest.mark.smoke
def test_login():
    assert True

@pytest.mark.regression
def test_payment():
    assert True

def is_even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

@pytest.mark.regression
def test_even():
    assert is_even_or_odd(4) == "Even"


def test_odd():
    assert is_even_or_odd(5) == "Odd"


## Skip and skipif

def add(a,b):
    return a+b

@pytest.mark.skip(reason="Feature not implemented yet")
def tetst_add():
    assert add(2,3) == 5

def is_even(n):
    return n%2 == 0

@pytest.mark.skipif(0 < 0 , reason="Neative number now allowed")
def test_negative_number():
    assert is_even(-5) == False


import pytest

# 🔹 Simple function
def is_even(n):
    return n % 2 == 0


# 🔹 1. Always skip
@pytest.mark.skip(reason="Feature not ready")
def test_skip_example():
    assert is_even(4) == True


# 🔹 2. Skip if condition is true
@pytest.mark.skipif(6 < 10, reason="Condition is true so skipping")
def test_skipif_example():
    assert is_even(5) == False


# 🔹 3. Dynamic skip using logic
def test_dynamic_skip():
    num = -2

    if num < 0:
        pytest.skip("Negative number not allowed")

    assert is_even(num) == True


# 🔹 4. Normal test (will run)
def test_even():
    assert is_even(10) == True


# 🔹 5. Another normal test
def test_odd():
    assert is_even(7) == False