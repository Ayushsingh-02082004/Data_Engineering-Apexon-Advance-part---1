class smartphone:
    def __init__(self , brand , batterylevel=50):
        self.brand = brand
        self.batterylevel = batterylevel

    def charge(self , amount):

        self.batterylevel += amount

        if self.batterylevel > 100:
            self.batterylevel = 100

        print("Amount should not exceede battery level above 100.")

    def __repr__(self):
        return f"Brand is {self.brand} battery is {self.batterylevel}"

phone = smartphone("mi")

phone.charge(20)
print(phone)