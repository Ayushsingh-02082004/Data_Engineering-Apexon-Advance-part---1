import pytest

def divide(a,b):
    return a / b

@pytest.mark.xfail(reason='diviide by zero is not handled' , strict=True)
def test_divide_by_zero():
    assert divide(1,0)  == 0

@pytest.mark.xfail(condition=True , reason="Known bug")
def test_sub_bug():
    result = 5-3
    assert result == 1