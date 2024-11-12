# LISTS

# foods = ["wings", "pizza", "mac n cheese", "salad", "sandwich"]
# food = "hamburger"
# some_items = ["desk", 23.4, True]
# nested_list = [[2, 4, 6], [1, 3, 5]]

# # Indexing
# print(foods[0])
# print(foods[-1])
# print(foods[3])

# print(foods[1:4])
# print(foods[1:])
# print(foods[:4:2])
# # print(foods[::-1])
# print(foods)
# foods.append("soup")
# print(foods)
# foods.extend(["gyro", 'steak'])
# print(foods)
# foods.insert(2, "hamburger")
# foods.remove("steak")
# print(foods)
# foods.pop(1)
# print(foods)
# print(len(foods))

# nums = [1, 3, 5, 6, 8, 9]
# print(sum(nums))
# print(max(nums))
# print(min(nums))

# text = "THIS IS A STRING"
# print(text.lower())
# foods.lower()

# foods = ["wings", "pizza", "pizza", "mac n cheese", "salad", "sandwich"]

# for food in foods:
#     print(food.upper())


# index = 0
# while index < len(foods):
#     print(foods[index])
#     index += 1
# print(list(range(5)))

# for index in range(len(foods)- 1): 
#     if foods[index] == foods[index +1]:
#         print("DUPLICATE!")

# print("pizza" in foods)
# print("bread" in foods)

def title_case(name):
    return name.title()

title_case()
names = ['brad', 'Nicole', 'samira', 'Jessica', 'Kantrell', 'Cieneh' ]

names = ['Brad', 'Nicole', 'Samira', 'Jessica', 'Kantrell', 'Cieneh' ]
names.sort()
print(names)
sorted_names = sorted(names, key=title_case )
print(sorted_names)



# TUPLES

tuple_1 = ("red", "blue")
str_1 = "brad"
print(tuple_1)
tuple_1 += "green", "orange"
str_1 += " likes pizza"
print(tuple_1)
print(str_1)
num = 1
num += 1

print(tuple_1[0:3])

for color in tuple_1:
    print(color)


empty_tuple = ()
# must have the trailing comma
single_tuple = 8,

WEEK_DAYS = ("Mon", "Tue", "Wed", "Thurs", "Fri")


sorted_days = sorted(WEEK_DAYS)
print(sorted_days)
print(tuple(sorted_days))

foods = ("wings", "pizza", "pizza", "mac n cheese", "salad", "sandwich")

# print(list(enumerate(foods)))

for index, food in enumerate(foods, 1):
    print(f"{index}. {food}")


# def sum_average
col_1, col_2, col_3, col_4 = ("orange", 'red', "green", "blue")
# print(col_1, col_2, col_3, col_4)


def sum_and_average(nums):
    num_sum = sum(nums)
    average = num_sum / len(nums)
    return (num_sum, average)

sol_sum, sol_avg = sum_and_average([1, 2, 3, 4, 5])
print(sol_avg, sol_sum)

# DICTIONARIES
nums = [1, 2, 3, 4]

post_1 = {
    "name": "Brad",
    "age": 46,
    4: [1, 2, 3, 4],
    "username": "brads213",
    True: True,
    (1, 2): "submaring"
}

print(post_1)
print(post_1["bio"])
print("bio" in post_1)

print(post_1.get("name"))
print(post_1.get("bio"))
print(post_1["age"])
post_1["age"] = 47
print(post_1)

# if "name" not in post_1:
#     post_1["name"] = "Mike"

del post_1[True]
print(post_1)


# print(post_1.keys())
# print(post_1.values())
# print(post_1.items())


# for key in post_1.keys():
#     print(key)
   

# for value in post_1.values():
#     print(value)

# for key, value in post_1.items():
#     print(key, value)


feed = [
    {
    "username": "brads",
    "date": "10/8/24",
    "caption": "Looks like a great day!",
    },
    {
    "username": "nicoleG",
    "date": "10/7/24",
    "caption": "can't wait for coding class tomorrow!",
    "ingredients": ["flour", "sugar"],
    "instructions": [
        "preheat oven to 400",
        "mix flour and sugar in a bowl",
    ]
    },
    {
    "username": "geraldS",
    "date": "10/6/24",
    "caption": "I love sundays"
    }
]

for post in feed:
    print(post)