import pytest
import re


def validate_productCode(code):
    pattern = r"^[A-Z]{2}-\d{4}$"
    if re.match(pattern , code):
        return True
    return False


@pytest.mark.parametrize("code , expected", [
    ("AB-3665",True),
    ("ab-3665",False),
    ("ABC-3665",False),
    ("ab1234-3665",False),
    ("AB665",False),
    ("A5",False),
    ("AB665",False),
    ("AY-2002",True)
])


# def test_product_codes(code , expected):
#     assert validate_productCode(code) == expected


def validate_email(email):
    pattern = r"^[\w]+\.[\w]+@[a-z]+\.[a-z]{2,}$"
    return bool(re.match(pattern , email))


@pytest.mark.parametrize("email , expected", [
    ("ayush.singh@bridgelabz.com", True),
    ("ayush.singh@bridgelabz.com", True),
    ("invlaid.@email.com", False),
    ("singh@bridgelabz.com", False),
    ("ayush@bridgelabz.com", False),
    ("ayh@bridgelabz.com", False),
    ("ayush.singridgelabz.com", False),
])

def test_email_variants(email, expected):
    assert validate_email(email) == expected