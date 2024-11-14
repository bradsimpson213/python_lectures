# list = [False, True, "2", 3, 4, 5]
# b = 0 not in list
# print(b)

# print( 0 == False)

# my_tuple = (1, 2, 3)
# my_tuple = (True, False)

# print(my_tuple[1])

# my_tuple[1] = "Hello"

# x = [0, 1, 2]
# x.insert(0, 1)
# del x[1]
# print(sum(x))

# list1 = [1, 3]   # ------>  m1 & m2
# list1 = list2
# list2 = [*list1]  #  ------> m3 & m4
# list1[0] = 4
# print(list1, list2)

# list[start:stop(not inclusive):step]
# defaults  list[::-1]

# nums = [1, 2, 3]
# vals = nums
# del vals[1]
# print("NUMS", nums, "VALS", vals)

# dct = {}
# dct["1"] = (1, 2)
# dct["2"] = (2, 1)
# print(dct)
# print(dct.keys())
# for x in dct.keys():
#     print(dct[x][1], end="")

# print("hello!")

# print(dct["1"])
# print((1, 2)[1])

# print(list("hello"))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(nums[-2])
# print(nums[:])
# print(nums[1:5])
# print(nums[::-9])

# dct = {}
# dct[1] = 1
# dct["1"] = 2
# dct[1] += 1
# print(dct)

# some_sum = 0

# for k in dct:
#     some_sum += dct[k]

# print(some_sum)

# dictionary = {
#     "one": "two", 
#     "three": "one", 
#     "two": "three"
# }
# v = dictionary["one"] # set v = "two"
# print(dictionary, v)

# for k in range(len(dictionary)):
#     v = divtionary[v]
#     print(k, v)


# print(v)

# str1 = "Peter"
# str2 = str1[:]

# print(id(str1))
# print(id(str2))
# print(str1 == str2)

# print(True == 1)
# print(1 == 1.0000)
# print(True is 1)

# list_1 = [1, 4,  2, 3]
# list_2 -= list1

# data = ((1, 2), ) * 7
# print(data)
# print(len(data[3:8]))

# ages = {"Peter": 30, "Paul": 31}
# print(list(ages.values()))

# tup = (1,) + (1,)
# print(tup)
# tup = tup + tup
# print(len(tup))

# brad = "Brad"
# brad = brad + brad
# print(brad)

# data = (1, 2, 4, 8)
# data = data[-2:-1]
# print(data)
# data = data[-1]
# print(data)

# my_list = [1, 2, 3]
# # print(list(range(2)))
# for v in range(2):
#     my_list.insert(-1, my_list[v])
#     print(my_list)

# print(my_list)

# response = "try , except"

def find_max(nums):
    max_num = 0
    for num in nums:
        if max_num < num:
            max_num = num
    
    return max_num


# print(find_max([1, 2]))

# print(bin(True))
# print(bin(1))
# print(bin(False))
# print(bin(0))
# print(123_456)

# PEMDAS

# index[-1:1:1]
# range(-1, 1, 1)

# others = 1
# for i in range(2, 4):  #[2, 3]
#     for j in range(-1, 2): # [-1, 0, 1]
#         print('I', i, 'J', j)
#         if i == j:
#             others += 1
#         else:
#             break

# print(others)

# angle = -1
# for i in range(-1, 1): #[-1, 0]
#     if 2 * i < 4:
#         angle += 1
#     else: 
#         angle += 2

# print(angle)

# power = 2

# while power < 5:  # 1:2  2:3 3:4
#     power += 1  # 1:3 2:4 3:5
#     if power == 3:
#         continue
#     print("@", end="")
    
# print("@") 

# torque = 0
# print("first Torque", torque != 0)
# while torque != 0:
#     torque //= 2
#     print("TORQUE", torque)
#     print("*", end="")
# else:
#     print("*")

# train_speed = {
#     'FlyingScotsman': 201,
#     'TGV': 320,
#     'Shinkansen': 320
# }
# print(train_speed.items())
# for train in train_speed.items():
#     print(train[0], end="")

# numbers = [1, 0.5, 0.25, 0.125]

# print(numbers[:])

# answers = (False, True, True, False, True)
# selection = answers[:]
# print(selection)
# points = 0
# for potato in selection:
#     if potato:
#         points +=1

# print(points)

# 2 0 3 1


# the_data = [True, 3.1415, -2]

# print(len(the_data[0:2]) == 0)
# # print(-2 in the_data[2:4])
# print(the_data.index(-2) not in the_data)
# print(the_data.index(the_data[-1]) == 0)


# new_tup = (1, True, "Pizza")
# other_tuple = (1, 2) + (2, 3)
# other_tuple += (4, 5)
# print(other_tuple)
# print("Brad loves" + " pizza")

# def walk(top):
#     if top == 0:
#         return 0
#     else:
#         return top + walk(top - 1)
#               2       1
# print(walk(2))
# walk ----> arg 2  return 2 + 1
# walkx2 ----> arg 1 return 1 + 0
# walkx3 ----> arg 0 return 0#

# def recursive_interating(lst):
#     print("START of function", lst)
#     if len(lst) == 0:
#         return 
#     else:
#         print(lst[0])
#         recursive_interating(lst[1:])

# recursive_interating([5, 4, 3, 2, 1])

# def sample(value):
#     return total + value

# total = 4
# total = sample(2)  # saves total = 6
# total = sample(1)   # saves total = 7
# print(total)


# data = {"name": "Peter", 'age': 30}
# person = data.copy()
# print(id(data) == id(person))

list_1 = ["A", 2, 7, 1, 4]
# list_1.reverse()
print(list_1[::-1])