import re

string = "2004 02 , 0208 2004"
pattern = "(\d{3}) (\d{2})"

match = re.search(pattern , string)

if match:
    print(match.group())
else:
    print("Pattern not found")