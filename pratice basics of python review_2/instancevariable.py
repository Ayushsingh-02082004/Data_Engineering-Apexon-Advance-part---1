class BankAccount:

    Bank = "Baroda Uttar Pradesh Gramin Bank"

    def __init__(self , holdername , balance):
        self.holdername = holdername
        self.balance = balance


c1 = BankAccount("yushii" , 90000)
c2 = BankAccount("piyush" , 80000)

customerx = BankAccount("x" , 100000)


print(f"coustmer1 NAME_ {c1.holdername} BALANCE_ {c1.balance} in BANK _ {c1.Bank}")

print(f"customer x {customerx.holdername} and his balance is {customerx.balance} in Bank {customerx.Bank}")