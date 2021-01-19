print("This is a madlibs program!")
print("___(name)__ ate so many ___(food)__ for breakfast.")
user_input1 = input("Please enter a name: ")
user_input2 = input("Please enter a food: ")

def madlib(sub1, sub2):
    return print(f"{sub1} ate so many {sub2} for breakfast. ")

madlib(user_input1, user_input2)