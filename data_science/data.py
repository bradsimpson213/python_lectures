
# from datetime import datetime

# start = datetime.now()
# # print(start)
# count = 0
# for num in range(1_000_000_000):
#     count += 1
# print(count)

# end = datetime.now()
# print("how long it took:", end - start)

# 2d List
# list_2d = [
#     [1, 2, 3, 4],
#     [4, 5, 6, 4],
# ]

# print(list_2d[0][1])

import numpy as np

# my_list = [1, 2, 3, 4, 5]
# # print(my_list)
# arr_1 = np.array(my_list)
# # print("arr_1", arr_1)
# arr_2 = np.array(list_2d)
# # print("arr_2", arr_2)
# arr_3 = np.arange(0, 10, 1)
# print(arr_3)
# print(arr_3[2:5])

# print(arr_2[1 , 2])


# Tic Tac Toe

# board = np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])
# print(board)
# board[1, 1] = "X"
# print(board)
# board[0, 2] = "O"
# print(board)
# board[0, 1] = "X"
# print(board)
# board[2, 1] = "O"
# print(board)
# board[0 , 0] = "X"
# print(board)
# board[1, 2] = "O"
# print(board)
# board[2, 2] = "X"
# print(board)

# list_1 = [1, 2, 3, 4]
# list_1_times4 = [ num * 4 for num in list_1]
# print(list_1_times4)
# list_2 = [5, 6, 7, 8]
# print(list_1 + list_2)
# print("Brad is hungry " + "for pizza!")

# arr_4 = np.array(list_1)
# arr_5 = np.array(list_2)
# print(arr_4 + arr_5)
# mult_arr = np.array([ 0 for _ in range(len(list_1))])
# print(mult_arr)
# mult_arr.fill(4)
# print(mult_arr)
# # print(arr_4 * mult_arr)
# mult_arr.fill(2)
# print(mult_arr)
# print(arr_4 * 5)
# print(arr_4 * mult_arr)

# print(np.sum(arr_4))
# print(np.min(arr_4))
# print(np.max(arr_4))

# PANDAS
import pandas as pd  

# data = {'foods': ["pizza", "hamburger", "salad"], 'calories': [800, 600, 200]} 
# df_1 = pd.DataFrame(data)
# print(df_1)

df_states = pd.read_csv('states.csv', names=["State Name", "Abbrev", "state_code"], header=0)
# print(df_states)
# print(df_states["State Name"])
# print(df_states.state_code)
# print(df_states.loc[1:3])


# print(df_states.iloc[1, 2])



df_netflix = pd.read_csv("netflix_titles.csv", sep="|", index_col=0)
# print(df_netflix)

df_countries = pd.read_csv("countries.csv", index_col=0)
# print(df_countries)
# Grouping
# data_2 = {'A': [1, 2, 3, 4, 5], 'B': ['foo', 'bar', 'baz', 'bar', 'foo']} 
# df_grouping = pd.DataFrame(data_2)
# print(df_grouping)
# grouped = df_grouping.groupby("B")
# print(grouped["A"].sum())


# print(df_state_pop.head(5))
# sorted_states = df_state_pop.sort_values("percent_of_total", inplace=True)
# # print(sorted_states)
# print(df_state_pop.head(5))

# print(df_state_pop.info())
# print(df_state_pop.columns)
# print(df_state_pop.size)
# print(df_state_pop.shape)
# print(df_state_pop.dtypes)
# print(df_state_pop[df_state_pop["2020_census"] > 20_000_000])
# # print(df_state_pop[df_state_pop["2020_census"].between(10_000_000, 25_000_000)])
# pops = [10077331, 9288994, 11799448, 6177224]
# # print(df_state_pop[df_state_pop["2020_census"].isin(pops)])
# ranks = [5.0, 6.0, 7.0]
# print(df_state_pop[df_state_pop["rank"].isin(ranks)])
# print(df_state_pop[df_state_pop["rank"].notna()])

# print(df_state_pop[ (df_state_pop["2020_census"] > 20_000_000) |(df_state_pop["2020_census"] < 5_000_000)])

# print(df_states)
df_state_pop = pd.read_csv("us_pop_by_state.csv")
# # print(df_state_pop)
merged_df = pd.merge(df_states, df_state_pop, on="state_code")
# # print(merged_df)
# # print(merged_df.drop(labels="state", axis=1))
merged_df.drop(columns="state", inplace=True)
# # print(merged_df)
merged_df.rename(columns={ "2020_census": 'Population'}, inplace=True)
# # print(merged_df.drop(index=8, axis=0))
print(merged_df)
# merged_df["State Animal"] = "cat"
# merged_df.insert(3, 'State Flag', "flag")
# print(merged_df)

df_houses = pd.read_csv("house_data.csv")
# print(df_houses)
# print(df_houses.info())
df_houses["total_rooms"] = df_houses["bedrooms"] + df_houses["bathrooms"]
# print(df_houses[["bedrooms", "bathrooms", "total_rooms"]].sum())
# print(df_houses.max())
# print(df_houses.min())


# MATPLOTLIB
import matplotlib.pyplot as plt

# Line plots
print(plt.style.available)
plt.style.use("fivethirtyeight")
plt.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], color="green", linewidth=4, label="Green plot")
plt.plot([1, 2, 3, 4, 5], [4, 8, 12, 16, 20], color="orange", linestyle="--", label="Orange Plot")
plt.title("Line Plot Example")
plt.xlabel("X Series")
plt.ylabel("Y Series")
plt.legend()
# plt.yticks([6, 12], labels=["6K", "12k"])
# plt.xticks([2, 4, 6, 8])
plt.show()

# Bar plots
# foods = ["pizza", "burgers", "wings", "salad"]
# times_prepared = [45, 67, 24, 13]
# times_ruined = [3, 6, 1, 3]
# plt.bar(foods, times_prepared, label="Made delicious")
# plt.bar(foods, times_ruined, label="Made not good", bottom=times_prepared)
# # plt.barh(foods, times_prepared, label="Made delicious")
# # plt.barh(foods, times_ruined, label="Made not good", left=times_prepared)
# plt.legend()
# plt.title("Brads Food Prep")
# # plt.xlabel('Food Cooked')
# # plt.ylabel('Times Prepared')
# plt.ylabel('Food Cooked')
# plt.xlabel('Times Prepared')
# plt.show()

# Histograms
# test_scores = [ 66, 77, 78, 78, 88, 91, 77, 78, 95, 78, 85, 81, 61, 78, 77, 68, 81, 83, 74]
# plt.hist(test_scores, bins=10)
# plt.title("Dist of Test Scores")
# plt.show()

# Scatter
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 8]
# plt.scatter(x, x, marker="p", color='red', label="Cogs")
# plt.scatter(x, y, marker="D", color="blue", label="Sprockets")
# plt.legend()
# plt.show()

# Pie
# labels = ["Building Improvements", "Deferred Maintenance", "Contractor Fees", "Taxes", "Site Improvements" ]
# costs = [47_945_970, 3_752_581, 7_340_612, 3_233_392, 18_345_789]
# # plt.figure(figsize=(10,4))
# plt.pie(costs, labels=labels, autopct='%1.2f%%', explode=(0,0.5,0,0.1,0))
# plt.title("Site Cost Breakdown")
# plt.show()

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# data_2 = [
#     [2, 4, 6, 8, 10, 12, 14],
#     [1, 4, 4, 5, 5, 6, 6, 7, 7, 8, 12],
#     [1, 2, 2, 3, 3, 7],
# ]
# plt.boxplot(data_2)
# plt.title('Box Plot')
# plt.show()

# Subplots
# plt.figure(figsize=(10,4))
# plt.suptitle("Brads Many Charts")

# plt.subplot(1, 3, 1)
# foods = ["pizza", "burgers", "wings", "salad"]
# times_prepared = [45, 67, 24, 13]
# times_ruined = [3, 6, 1, 3]
# plt.bar(foods, times_prepared, label="Made delicious")
# plt.bar(foods, times_ruined, label="Made not good", bottom=times_prepared)
# plt.legend()
# plt.title("Brads Food Prep")
# plt.xlabel('Food Cooked')
# plt.ylabel('Times Prepared')

# plt.subplot(1, 3, 2)
# test_scores = [ 66, 77, 78, 78, 88, 91, 77, 78, 95, 78, 85, 81, 61, 78, 77, 68, 81, 83, 74]
# plt.hist(test_scores, bins=4, color="green")
# plt.title("Dist of Test Scores")
# plt.xlabel('Test Score')
# plt.ylabel('Frequency')

# plt.subplot(1, 3, 3)
# labels = ["Building Improvements", "Deferred Maintenance", "Contractor Fees", "Taxes", "Site Improvements" ]
# costs = [47_945_970, 3_752_581, 7_340_612, 3_233_392, 18_345_789]
# plt.pie(costs, labels=labels, autopct='%1.0f%%', explode=(0,0.2,0,0.1,0))
# plt.title("Site Cost Breakdown")
# plt.show()
# plt.subplot(2, 2, 4)
# data_2 = [
#     [2, 4, 6, 8, 10, 12, 14],
#     [1, 4, 4, 5, 5, 6, 6, 7, 7, 8, 12],
#     [1, 2, 2, 3, 3, 7],
# ]
# plt.boxplot(data_2)
# plt.title('Box Plot')
# plt.show()

# nums = np.arange(10)
# print(nums)
# plt.figure(figsize=(10,4))
# plt.suptitle("Num Plots")
# plt.subplot(1, 3, 1)
# plt.title("Nums")
# plt.plot(nums, nums, color="blue", label="Nums")
# plt.subplot(1, 3, 2)
# plt.title("Nums Squared")
# plt.plot(nums, nums**2, color="red", label="Nums Squared")
# plt.subplot(1, 3, 3)
# plt.title("Nums Cubed")
# plt.plot(nums, nums**3, color="orange", label="Nums Cubed")
# plt.show()

# rng = np.random.default_rng()
# data = rng.integers(60, high=100, size=100)
# print(data)
# plt.hist(data, bins=20)
# plt.show()

# print(merged_df["State Name"].head(10))
# plt.figure(figsize=(10, 4))
# plt.title("Pop by State")
# plt.bar(merged_df["State Name"].head(10), merged_df['Population'].head(10))
# plt.ylabel("People in 10M")
# plt.show()

labels = ["Napping", "Sleeping", "Eating", "Purring", "Looking Cute" ]
costs = [34.32, 35.23, 10.43, 12.32, 7.71 ]
plt.figure(figsize=(5,4))
plt.pie(costs, labels=labels, autopct='%1.0f%%', explode=(0,0,0.1,0,0))
plt.title("28 Elberon Cat Activities")
plt.show()