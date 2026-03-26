#-------------Formatting Decorator----------------
def make_pretty(func):
    def wrapper(*args , **kwargs):
        print("=" * 30)
        func(*args , **kwargs)
        print("=" * 30)
    return wrapper

@make_pretty
def display_menu():
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Exit")

# display_menu()


#---------------Security Decorator---------------

def require_pin(func):
    def wrapper(*args , **kwargs):
        userpin = input("Enter you 4-digit PIN to proceed: ")
        if userpin == "1234":
            return func(*args , **kwargs)
        else:print("!!! Access Denied: Incorrect PIN !!!")
    return wrapper

@require_pin
def withdraw_cash(amount):
    print(f"Success! Dispensing ${amount}...")


# withdraw_cash(500)

#-----------The counter Decorator----------

def count_calls(func):
    def wrapper(*args , **kwargs):
        wrapper.count += 1
        print(f"Call number {wrapper.count} for {func.__name__}")
        return func(*args , **kwargs)
    
    wrapper.count = 0 #initializing the counter
    return wrapper


@count_calls
def roll_dice():
    print("Dice rolled!")

roll_dice()
roll_dice()
roll_dice()