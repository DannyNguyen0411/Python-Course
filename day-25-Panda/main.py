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

# Get Data in Row
print(data[data.day == "Monday"])

max_temperature = data[data.temp == data.temp.max()]
print(max_temperature)

monday = data[data.day == "Monday"]
print(monday.condition)

# # Warmest day of the week
# max_temp = data["temp"].max()
#
# if max_temp == data["temp"].max:
#     print(data["temp"].max)




