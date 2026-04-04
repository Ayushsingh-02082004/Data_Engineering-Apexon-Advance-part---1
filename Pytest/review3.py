import re


# Password validator


def password_validator(password):
     pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[^\s]{8,}$"

     return re.match(pattern , password) 


def test_valid_password():
     assert password_validator("Ayush@0346")
     assert password_validator("Piyush@9956")

    #  assert not password_validator("agh8ahihi")
    #  assert not password_validator("9818678790")




#    Indian phone number extractor


def extract_indian_numbers(text):

    pattern = r"(?:\+91[-\s]?|0)?[6-9]\d{9}"
    return re.findall(pattern , text)


def test_indian_no():
       text = "Call +91-9876543210 or 9123456789 or 1234567890"

       result = extract_indian_numbers(text)
    #    assert "9876543210" in result
       assert "+91-9876543210" in result


        #VAlid Email


def is_valid_email(email):

    pattern = r"^(?!.*\.\.)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})+$"
    return re.match(pattern , email) 


def test_email_valid():
    assert is_valid_email("ayush.singh@gmail.com")
    assert is_valid_email("ayush0346.be21@chitkara.edu.in")


def test_email_not_valid():
    assert not is_valid_email("user__..@gmail.com")
    assert not is_valid_email("ayush@singh")

