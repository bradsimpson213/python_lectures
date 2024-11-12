import os

# str(1) # "1"
# round(2.44)
# name = "Brad"


print(round)
def calculator():
    '''a simple calculator provide 2 numbers and an 
    operator to make your calculation'''

    os.system('clear')
    print("Welcome to the calculator app!")

    calc_on = True

    while calc_on:
        num_1 = float(input("Whats the first number?: "))
        oper = input("Pick your operator ['+','-','*','/']?: ")
        num_2 = float(input("Whats the second number?: "))


        if oper == "+": 
            print(f"{num_1} + {num_2} = {num_1 + num_2}")
        elif oper == "-":
            print(f"{num_1} - {num_2} = {num_1 - num_2}")
        elif oper == "*":
            print(f"{num_1} * {num_2} = {num_1 * num_2}")
        elif oper == "/":
            print(f"{num_1} / {num_2} = {num_1 / num_2}")
        else:
            print("Inccorect input, try again!")
            continue

        again = input("Do you want to calculate again?  [Y or N]?: ").lower()
        if again == "y":
            continue
        else:
            calc_on = False


calculator()
# help(calculator)

