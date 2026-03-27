import re


String = "Hey this is my college id ayushsingh0346.be21@chitkara.edu.in and this is my personal id ayushsingh02082004@gmail.com and this is my company's gmail id ayush.singh@bridgelabz.com extract gamil out of this"

# pattern = r"\b[\w\.]+@[a-z]+\.[a-z]{3}[\.a-z]*\b"
pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

result = re.findall(pattern , String)

print(result)ds