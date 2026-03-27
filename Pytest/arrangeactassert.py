import math

def mul(a,b):
    return math.prod([a,b])

def test_aaa():
    # arrange
    a = 8
    b = 9

    #act
    result = mul(a,b)

    #assert
    assert result == 72