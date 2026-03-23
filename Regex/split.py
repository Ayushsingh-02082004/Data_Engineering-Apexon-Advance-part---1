import re

string = "Hey i am ayush for sure i will do something great in life before 30."
pattern = " "

result = re.split(pattern , string , 5)
print(result)
