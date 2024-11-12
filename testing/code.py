
def add(x, y):
    return x + y


def enough_donuts(num_donuts):
    if num_donuts < 0:
        return "No donuts on credit, we must use positive integers"
    elif num_donuts >= 0 and num_donuts <= 1:
        return "Not enough donuts"     
    elif num_donuts > 1 and num_donuts <= 4:
        return "That's enough donuts" 
    elif num_donuts > 4 and num_donuts <= 12:
        return  "That's a lot of donuts"
    else:
        return  "I hope you are sharing"


answer = input('What character do we use to index in python?: ')
if answer == "brackets":
    print("Correct!")
else:
    print("Wrong answer")