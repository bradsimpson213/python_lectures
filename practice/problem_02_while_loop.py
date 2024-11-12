# PROBLEM 2 - WHILE LOOP: Sort out the odd numbers...
#
# In this problem, write a function named "while_loop_odds" that accepts an
# iterable of integers as a parameter and returns a new list with only the odd
# numbers from the original list.
#
# *The function MUST use a WHILE LOOP in its implementation.
#
#
#
#  ______________________________YOUR CODE BELOW______________________________#

def while_loop_odds(int_list):
    odds_list = []
    index = 0

    while index < len(int_list):
        if int_list[index] % 2 != 0:
            odds_list.append(int_list[index])
        
        index += 1

    return odds_list


# __________SAMPLE TEST DATA__________ #
lst1 = [1,2,4,5,7,9]
print(while_loop_odds(lst1))      # [1, 5, 7, 9]
lst2 = [2, 3, 4, 5, 6, 7]
print(while_loop_odds(lst2))      # [3, 5, 7]
