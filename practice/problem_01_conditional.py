# PROBLEM 1 - IF STATEMENTS: Too many donuts... 🍩 🍩 🍩
#
# In this problem, write a function named "enough_donuts" that takes an integer
# parameter and returns the corresponding string value found in this table
#
#  -------------------------------------------------------------------------
# | Input                                        | Output                   |
# |----------------------------------------------|--------------------------|
# | Less than or equal to 1                      | "Not enough donuts"      |
# | Greater than 1 and less than or equal to 4   | "That's enough donuts"   |
# | Greater than 4 and less than or equal to 12  | "That's a lot of donuts" |
# | Greater than 12                              | "I hope you are sharing" |
#  -------------------------------------------------------------------------
#
# Your code MUST include at least one of each of the following keywords:
#
# * if
# * elif
# * else
#
# All inputs are guaranteed to be greater than 0.
#
#

#
#  ______________________________YOUR CODE BELOW______________________________#

def enough_donuts(num_donuts):

    if num_donuts <= 1:
        return "Not enough donuts"     
    elif num_donuts > 1 and num_donuts <= 4:
        return "That's enough donuts" 
    elif num_donuts > 4 and num_donuts <= 12:
        return  "That's a lot of donuts"
    else:
        return  "I hope you are sharing"

# __________SAMPLE TEST DATA__________ #
# print(enough_donuts(1))       # Not enough donuts
# print(enough_donuts(4))       # That's enough donuts
# print(enough_donuts(14))      # I hope you are sharing


result_1 = enough_donuts(1)
result_2 = enough_donuts(4)       
result_3 = enough_donuts(14) 

if result_1 == "Not enough donuts":
    print("Test 1 passed!")
else:
    print('Test 1 failed, we should look in to that...')

if result_2 == "That's enough donuts" :
    print("Test 2 passed!")
else:
    print('Test 2 failed, we should look in to that...')

if result_3 == "I hope you are sharing":
    print("Test 3 passed!")
else:
    print('Test 3 failed, we should look in to that...')



