#Hey ayush today i will tell you how to use match functions.


import re

text = " I love Mahadev. shiva."
 
match  = re.search(r"Mahadev" , text)

if match:
    print(f"1 . Start Index: {match.start()}")
    print(f"2 . End Index: {match.end()}")
    print(f"3 . Span Tuple: {match.span()}")
    print(f"4. The String: {match.string}")