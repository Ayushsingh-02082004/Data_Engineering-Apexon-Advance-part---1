import pytest

@pytest.fixture
def data():
    return 10


def test_one(data):
    assert data  == 10

def test_tow(data):
    assert data == 10

@pytest.fixture(params=["Apple" , "FireFox", "Banana" , "Mango"])
def browser(request):
    return request.param

def test_browser_launch(browser):
    print(f"Running Test on : {browser}")
    assert browser in ["Apple" , "FireFox", "Banana" ,"Edge"]