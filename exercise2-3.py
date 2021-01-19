print("This program is a temperature converter!")

user_decision = input("Would you like to enter a number in Celsius or Fahrenheit? ")

user_input = float(input("Please enter a temperature: "))
def tempc_converter(input1):
    F = (input1 * 9/5) + 32
    F1 = str(F) + " F"
    print(F1)

def tempf_converter(input2):
    C = (input2 - 32) * 5/9
    C1 = str(C) + " C"
    print(C1)

if user_decision == "celsius":
    tempc_converter(user_input)
    
else: 
    user_decision == "fahrenheit"
    tempf_converter(user_input)
