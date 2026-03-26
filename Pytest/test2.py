import pytest

# 🔹 Simple function
def is_even(n):
    return n % 2 == 0


# 🔹 1. Always skip
@pytest.mark.skip(reason="Feature not ready")
def test_skip_example():
    assert is_even(4) == True


# 🔹 2. Skip if condition is true
@pytest.mark.skipif(20 < 10, reason="Condition is true so skipping")
def test_skipif_example():
    assert is_even(20) == True


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