
name = input("Enter your name :")
year = input("Enter the birht year : ")

result = name.replace(" " , "").lower()

result = result[:3] + year

print(result)