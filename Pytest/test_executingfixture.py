import pytest

@pytest.fixture
def setup_environment():

    #setup code
    print("Setting up environment")
    yield("Environment is ready for Testing")
    #teardown code
    print("tearing down environment")


def test_example_action(setup_environment):
    print(f"Executing myfirst test with fixture : {setup_environment}")
    assert setup_environment  == "Environment is ready for Testing"


def test_example_action(setup_environment):
    print(f"EXecuting anohter test with fixture: {setup_environment}")
    assert setup_environment == "Environment is ready for Testing"