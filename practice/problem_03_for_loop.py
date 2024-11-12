# PROBLEM 3 - FOR LOOP: Sort out the even numbers...
#
# In this problem, write a function named "for_loop_evens" that accepts an
# iterable of integers as a parameter and returns a new list with only the even
# numbers from the original list.
#
# *The function MUST use a FOR LOOP in its implementation.
#
#
#  ______________________________YOUR CODE BELOW______________________________#

def for_loop_evens(int_list):
    """ accepts a iterable of integers and returns a new 
    list of only even integers """
    evens_list = []

    for num in int_list:
        print("num in for loop", num)
        # need to use modulo to check for evens
        if num % 2 == 0:
            print("we got inside the if statement")
            evens_list.append(num)
    print("EVENS LIST!!!", evens_list)
    return evens_list

# __________SAMPLE TEST DATA__________ #
lst1 = [1,2,4,5,7,9]
print(for_loop_evens(lst1))       # [2, 4]
lst2 = [2, 3, 4, 5, 6, 7]
print(for_loop_evens(lst2))       # [2, 4, 6]
