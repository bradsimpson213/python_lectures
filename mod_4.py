
patient_1 = {
    "name": "Brad",
    "age": 46,
    "phone": "201-234-123",
    "DOB": "12/23/1978"
}

patient_2 = {
    "name": "Brad",
    "age": 46,
    "phone_number": 2012495656,
    "DOB": "12/23/1978"
}

# class Patient:

#     def grow_older()
#         age += 1
    

# brad = Patient("Brad", 46, "234-234-2344", "11/11/11")
# # # # patient_2 = { "name": "Patch", "age": 8, "phone": "none", "DOB": "6/11/2022" }


# # # patient_info = [patient_1, patient_2]

# # # def get_DOB(patient):
# # #     return patient["DOB"]


# # # [{},{},{}]

# # # sorted_patients = sorted(patient_info, key=['DOB'])
# # # print(sorted_patients)

# # # for patient in patient_info:
# # #     print(patient["name"])

# # # test_list = [1, 2, 3, "brad"]

# patient_info2 = [
#     {
#         "name": "Brad",
#         "age": 46,
#         "phone": "201-234-123",
#         "DOB": "12/23/1978",
#         "allergies": ["Penicillin", "Omoxicillin"],
#     },
#     { "name": "Patch", "age": 8, "phone": "none", "DOB": "6/11/2022" }
# ]

# # new_patient = Patient('Brad', 46, "")
# # # print(patient_info2[0]["allergies"][0])

# # # patient_123 = {
# # #         "patient_id": 12345123454
# # #         "name": "Andy",
# # #         "age": 11,
# # #         "phone": "201-234-123",
# # #         "DOB": "11/11/2011",
# # #         "allergies": [],
# # #         "dependantss": []
# # # }


# # # patient_234 =     {
# # #         "name": "Brad",
# # #         "age": 46,
# # #         "mood": "😁"
# # #         "phone": "(201) 234-123",
# # #         "DOB": "12/23/1978",
# # #         "allergies": ["Penicillin***", "Omoxicillin"],
# # #         "dependantss": [ patient_123 ],
# # # }



# # more_info = {
# #     "bio": "Brad is great",
# #     "address": "1 Main St"
# # }

# # # patient_dict["bio"] = "Brad is great."
# # patient_dict.update(more_info)
# # print(patient_234)

# # patients = {
# #     1234: {
# #         "name": "Andy",
# #         "age": 11,
# #         "phone": "201-234-123",
# #         "DOB": "11/11/2011",
# #         "allergies": [],
# #         "dependantss": []
# #     },
# #     1235: {
# #         "name": "Brad",
# #         "age": 46,
# #         "phone": "201-234-123",
# #         "DOB": "12/23/1978",
# #         "allergies": ["Penicillin", "Omoxicillin"],
# #         "dependantss": [ patient_123 ],
# #     }
# # }


# # nums = [1, 2, 3, 4, 5]
# # nums_2 = [ *nums ]

# # print(nums_2)

# # my_dict = {
# #     "name": "Brad",
# #     "age": 46
# # }

# # my_other_type = {**my_dict}
# # print("other_vals", my_other_type)

# # SETS
# my_not_a_set = {}  # empty dictionary
# my_set = set() 
# my_set_2 = {1, 2}
# print(my_set_2)

# my_nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
# my_letters = ["a", "a", 'b', 'B', 'c', 'd', 'e', 'e']
# # print(list(set(my_nums)))
# print(my_letters)
# print(set(my_letters))
# print(tuple(my_letters))

# another_set = {1, 1, 2, 2, 3}
# print(another_set)

# my_new_set = {1, 4, "hello", True}
# print(my_new_set)
# my_new_set.add("5")
# print(my_new_set)
# print("5" in my_new_set)
# my_new_set.update({6, 4, "world"})
# print(my_new_set)
# my_new_set.remove(True)
# print(my_new_set)

# for val in my_new_set:
#     print(val)

# set_1 = {1, 2, 3, 4, 5}
# set_2 = {4, 5, 6, 7, 8}

# # UNION
# print(set_1 | set_2)
# print(set_1.union(set_2))

# # # INTERSECTION
# print( set_1 & set_2 )
# print(set_1.intersection(set_2))

# # # DIFFERENCE
# print(set_1 - set_2)
# print(set_2 - set_1)
# print(set_1.difference(set_2))

# # # SYMETRIC DIFFERESD
# print(set_1 ^ set_2)
# print(set_1.symmetric_difference(set_2))


# def save_the_world():
#     print("Hey we are good, world saved")

# # # TRY EXCEPT

# print(list_1)
# raise Exception("This was an error, oopsies!")
# list_1 = [1, 2, 3, 4]
# print(list_1[5]) 


num = 0

try:
    print("We are in the try block")
    print(5/num)

except ZeroDivisionError:
    print("We can't divide by zero!")
    print(f"Maybe you wanted to divide by 1 instead? that would have been {5/1}")

except TypeError:
    print("We can't do math with strings, lets try a number")

# except:
#     print("You have made an error...")

else:
    print("Only going to see this if the try is successful")

finally:
    print("We will always see this")


save_the_world()


# # None
# vals = [1, "two", True, None]

# data = None

# def manipulate_data():
#     global data



# meals = {
#     "breakfast": "eggs", 
#     "lunch": "sandwich", 
#     "dinner": "steak",
#     "dessert": "cake"
# }

# meals["dinner"] = "muffin"

# # print(meals)
# # print(meals["dessert"])
# # print(meals.get("dessert"))
# if meals.get("dessert") == None:
#      meals["dessert"] = "apple pie"
#      print(meals)
# else:
#     print("Key already exists!")


# def new_function():
#     print("Hello")


# print(new_function())
    
# # val = None
# # print(val)

# # List Comprehensions
# vals = [1, 2, 3, 4, 5, 6, 7]
# letters = ['a', 'b', 'c']
# for val in vals:
#     print(val)

# copy_vals = [val for val in vals]
# print(copy_vals)
# copy_2_vals = [*vals]
# print(copy_2_vals)
# def doubler(num):
#     return num * 2

# vals_times2 = [ doubler(val)  for val in vals]
# print(vals_times2)

# new_vals = []
# for val in vals:
#     new_vals.append(val * 2)

# letters_upper = [ letter.upper() for letter in letters]
# print(letters_upper)

# evens = [ val * 2 for val in vals if val % 2 == 0]
# print(evens)
# odds = [ val for val in vals if val % 2 != 0]
# print(odds)

# if val == 0:
#     return val
# else:
#     return "sure"
# for index in range(len(vals) -1):
#     if vals[index] == vals[index + 1]:



# vals = [1, 3, 5, 7]
# print(vals)
# double_vals = [ val * 2 for val in vals]
# print(double_vals)

# # Files


# file = open("story.txt")
# print(list(file))
# help(file)
# content = file.read()
# print("print 1", content)
# file.seek(0)
# content2 = file.read()
# print("print 2", content2)
# more_content = file.readline()
# even_more_content = file.readline()
# print(more_content)
# print(even_more_content)

# all_content = file.readlines()
# print(all_content)
# cleaned_content = [line.rstrip() for line in all_content]
# print(cleaned_content)
# print(", ".join(cleaned_content))

# file = open("data.txt")
# all_content = file.readlines()
# print(all_content)
# clean_content = [int(num.rstrip()) for num in all_content]
# print(sum(clean_content))
# print(file.closed)
# file.close()
# print(file.closed)
# all_content = file.readlines()
# file = open("story.txt", "r+")
# content = file.read()
# print(content)
# file.seek(0)
# lines = [
#     "This is a story \n", 
#     "of a lovely lady...\n", 
#     "that was busy with 3 girls of her own..\n"
# ]
# file.writelines(lines)

# file.close()


# from random import choice as picker

# def choice():
# WITH

# with open("story.txt") as file:
#     print("closed?", file.closed)
#     content = file.read()
#     print(content)

# print("closed?", file.closed)


# SALES DATA PROBLEM
# Product,Type,Sales,
# T-Shirt,Clothing,100
# Jeans,Clothing,150
# Laptop,Electronics,500
# Mouse,Electronics,500
# Keyboard,Electronics,75
# Book,Books,30
# Pen,Stationery,10
# Notebook,Stationery,20
# item_1 = {
#     "Product": 'T-Shirt',
#     "Type": "Clothing",
#     "Price": 100
# }
# item_2 = {
#     "Product": 'Jeans',
#     "Type": "Clothing",
#     "Price": 150
# }

from csv import DictReader, writer

with open("sales_data.csv", 'r') as file:
    csv_file = DictReader(file)
    data = list(csv_file)
    print("data", data)

    sum_sales = {}

    for item in data:
        # print(item)
        if item["Type"] not in sum_sales:
            sum_sales[item["Type"]] = int(item["Sales"])
        else:
            sum_sales[item["Type"]] += int(item["Sales"])

    print("Sum sales: ", sum_sales)

    with open("sales_summary.csv", "w") as results:
        writer = writer(results)
        writer.writerow(["Category","TotalSales"])

        for key, value in sum_sales.items():
            writer.writerow([key, value])


    # print("num math", 100 + 100)
    # print("letter math", "100" + "100")
    # print("more string adding", "Brad likes " + "pizza")