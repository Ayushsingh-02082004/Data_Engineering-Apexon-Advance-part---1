import re

#Program to extract numbers from a string.

string = "Hello Ayush is 2002 born nut in aadhar its 2004 "
pattern = '\d+'

result = re.findall(pattern , string)
print(result)

