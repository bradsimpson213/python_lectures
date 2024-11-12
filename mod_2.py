

# # y = 20
# # brads_age = 46
# # y = 40 

# # PII = 3.14
# # DAYS = ("Mon", "Tues", "Weds", "Thurs", "Fri")


# # num = 20
# # num += 10  # num = 30  (20 + 10)
# # num = 30

# # count = 0

# # while count < 10:
# #     count += 1
# #     print(count)


# # print(10 / 2)
# # print(10 // 2)
# # print(10 / 3)
# # print(10 // 3)


# # print(3 == 3.0)
# # print(4 != 3)
# # print( 5 > 3)
# # print(6 >= 6)

# # print(1 == True)
# # print(0 == False)
# # print(bin(True))
# # print(bin(False))
# # print(1 is True)
# # print(0 is False)
# # print(4 == "4")

# # print(True and True)
# # print(True and False)
# # print(False and True)
# # print(False and False)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print(not True)
# print(not False)

# num_result = (10 + 20) * 30

# print(f"The sum was {num_result}")
# print(f"And doubled it is {num_result * 2}")
# print('This is just text')
# my_string = f"And doubled it is {num_result * 2}"
# print(len("my_string"))

# if len(my_string) < 10:
#     print("Yep less than 10")

# # if len(my_string) > 10 and len(my_string) > 20:
# #     print("Between 10 and 20")

# elif len(my_string) > 10 and len(my_string) > 20:
#     print("Between 10 and 20")

# else:
#     print("Not greater")



def is_even(num):
    """ takes in a number and returns 
    a boolean on if that number is even"""

    return num % 2 == 0


print(is_even(13))
# print(is_even(10))
# print(is_even(73))
# help(is_even)


num_1 = 50
PII = 3.14

print("global", num_1)

def function():
    global num_1
    print("function", num_1)
    num_1 -= 10
    print("function", num_1)

function()

print("global", num_1)

# nums = [5, 10, 15, 20, 25]
# print(sum(nums))
# print(min(nums))
# print(max(nums))

# print(int("24"))

# some_str = "pizza"
# print(some_str.upper())

from random import choice

from guessing import guessing_game

guessing_game()