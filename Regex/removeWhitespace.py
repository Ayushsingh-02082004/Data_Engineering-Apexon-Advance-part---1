import re

String = " Hey i am ayush previously i didnt believed in destin but now i do so , now i do believe in destiny."
pattern = "\s+"
replace = "_"

result = re.sub(pattern , replace , String)
print(result)