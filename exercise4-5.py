
user_input = int(input("Please enter a number to see if it's true: "))
def is_even(param1):
    if param1 % 2 == 0:
        return True 
    else:
        return False

def is_odd(param1):
    if is_even(param1):
        return False
    else:
        return True

print(is_odd(user_input))