string = "   !!!Error: System Failure 404!!!   "
string = string.replace("!" , "")
string  = string.replace("Error" , "Warning")
result = string.strip()


print(result)