# VARIABLES
# lunch = "Pizza is super tasty and I love it"
# print(lunch)
# print(lunch[0:4])
# print("Pizza weporiupoweirpoweirpoeiwproiewporipweoirpwoeirpowei")
# print("Pizza")
# total_pizzas = 10 + 4
# total_pizzas2 = 11 + 5
# total_pizzas = "pepperoni"


# BAD VARIABLE CHOICES
w = 12
q = "lunch"


# CONSTANT CONVENTION
TOTAL_PIZZAS = 20
PII = 3.14

# To check the location of a variable in memory
# print(id(total_pizzas))
# print(id(total_pizzas2))
# print(10 + 4)

# def pizza_maker(num):
#     return num * "pizza "

# print(pizza_maker(4))


# MATH STUFF
# my_int = 23
# my_float = 3.25
# my_big_int = 100_000_000_000
# print(my_big_int)
# my_tuple = 123,

# print(10 + 5)
# print(10 - 5)
# print(10 * 4)
# print(10 / 2)
# print(10 / 3)
# print (10 // 3)
# print(10 % 3)
# print(10 ** 2)

# count = 0
# print(count)
# count += 1
# print(count)
# count -= 1
# print(count)

# STRING STUFF
# my_string = "pizza's"
# my_other_string = 'soup'

# my_multiline_string = """
# this is a $%*%$&^%#&^% 😁
# multi line string
# so all spaces and new 
# lines get preserved
# """
# print(my_multiline_string)
# print(len(my_other_string))
# print(len(my_multiline_string))

# lunch = "soup"
# num_lunches = 2
# print(f"For lunch today I am going to have { num_lunches } { lunch.upper() }'s")

# STRING INDEXING
# food = "waffles"
# #       0123456
# print(food[2])
# # print(food[start:end:step])
# print(food[1:4])
# print(food[:5])
# print(food[::-1])


# IDENTITY vs EQUALITY
# print(5 == 5)
# print(5 == 4)
# print(4 != 3)
# print(4 == "4")

# NOT GOOD< BAD OUT
# print(True == 1)
# print(False == 0)

# print(True is 1)
# print(False is 0)

# print(bin(True))
# print(bin(False))

# var_1 = True
# print(id(var_1))
# var_2 = "Pizza"
# print(id(var_2))
# var_3 = True
# print(id(var_3))
# print(var_1 is var_3)

# HELP!
# help(str)

# CONTROL FLOW

def breakfast(food):

    if food == "waffles":
        print(f"{food.upper()} are the best breakfast food!")

    elif food == "pancakes":
        print(f"{food.upper()} are almost as good as waffles!")

    elif food == 'cereal':
        print("Ewww boring no one loves cereal")

    else:
        print(f"{food.upper()} are ok but not waffles")


    # if food == "pancake":

# breakfast("waffles")
# breakfast("pancake")
# breakfast("cereal")
# breakfast("eggs")


# ITERATING LOOPING

index = 1

while index < 5:
    if index == 3:
        print("We got a 3!!")
        break

    print("index", index)
    index += 1

print("While loop eneded, we are done")

# index = 0

while True:
    if index != 3:
        print(index)
        index += 1
        continue
    print("we found a 3")
    break


foods = ["pizza", 'sandwich', 'tacos', "salad"]

for food in foods:
     print(food.title())

# print("soda" in foods)
# print(list(range(6)))
# for index in range(len(foods)):
#     print(foods[index] == food[index + 1])





# GAME

import random
import os
from time import sleep

count = 99

while count < 1000: 
    os.system("clear")
    print(f"{count} little bugs in our code...")
    sleep(2.5)
    print(f"{count} pesky little bugs..")
    sleep(2.5)
    print("Take one down and patch it around")
    sleep(2.5)
    new_bugs = random.randint(1, 100)
    count += new_bugs
    print(f"{count} little bugs in our code!")
    sleep(2.5)


# guess = input("Please enter a number")


# guess = 5

# while gueses > 0:
#     # prompt for a guess
#     # compare guess to winning number
#     guess -= 1


# print("you lose")