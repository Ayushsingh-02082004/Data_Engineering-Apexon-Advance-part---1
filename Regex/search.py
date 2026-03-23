import re

string  = " Hey Ayush is a kind gentle and good boy."

match = re.search("\AAyush" , string)

if match:
    print("Pattern found inside the string")
else : 
    print("Pattern not found")