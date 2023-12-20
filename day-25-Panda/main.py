# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))


# average_temperature = data["temp"].mean()
# print(average_temperature)
#
# maximum_temperature = data["temp"].max()
# print(maximum_temperature)

# # The solution
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# # My solution
# number_of_temps = len(temp_list)
# total_temp = 0
# for temp in temp_list:
#     total_temp += temp
# average_temp = total_temp / number_of_temps
# print(f"The average temperature: {round(average_temp, 2)}")

# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# # Get Data in Row
# print(data[data.day == "Monday"])
#
# max_temperature = data[data.temp == data.temp.max()]
# print(max_temperature)


# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_fahrenheit = (monday_temp * 9 / 5) + 32
# print(monday_fahrenheit)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students" : ["Sonic", "Tails", "Knuckles"],
#     "scores" : [70, 100, 50]
# }
#
# data_students = pandas.DataFrame(data_dict)
# data_students.to_csv("new_data.csv")

data_squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231218.csv")

# # # Total squirrels 2968 in total.
# fur_color = data_squirrel["Primary Fur Color"]
# fur_color_counts = fur_color.value_counts()
# print(fur_color_counts)

grey_squirrels_count = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Cinnamon"])

data_dict_squirrels = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}

print(data_dict_squirrels)

data_info_squirrels = pandas.DataFrame(data_dict_squirrels)
data_info_squirrels.to_csv("squirrel_count.csv")

# fur_color_counts.to_csv("squirrel_count.csv")












