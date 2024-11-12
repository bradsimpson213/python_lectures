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

result_1 = enough_donuts(1)       # Not enough donuts
result_2 = enough_donuts(4)       # That's enough donuts
result_3 = enough_donuts(14)      # I hope you are shairing


if result_1 == "Not enough donuts":
    print("Test 1 successful!")
else:
    print("Test 1 failed")

if result_2 == "That's enough donuts":
    print("Test 2 successful!")
else:
    print("Test 2 failed")

if result_3 == "I hope you are sharing":
    print("Test 3 successful!")
else:
    print("Test 3 failed")