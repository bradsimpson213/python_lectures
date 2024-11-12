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

brad = "Brad"
brad = brad + brad
print(brad)

data = (1, 2, 4, 8)
data = data[-2:-1]
print(data)
data = data[-1]
print(data)

my_list = [1, 2, 3]
# print(list(range(2)))
for v in range(2):
    my_list.insert(-1, my_list[v])
    print(my_list)

print(my_list)