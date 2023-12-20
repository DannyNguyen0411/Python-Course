import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
#
# print(temp_list)
#
# #  Average temperature
# total_temp = sum(temp_list)
# amount_temp = (len(temp_list))
#
# average_temp = total_temp / amount_temp
# print(round(average_temp, 2))
#
# average_temp_mean = data.temp.mean()
# print(average_temp_mean)
#
# # Max value temperature
#
# max_temp = data.temp.max()
# print(max_temp)
#
# # Get data of column
# print(data.condition)

# # Get Data in Row
# print(data[data.temp == data.temp.max()])
# print(data[data.condition == "Sunny"])

data_monday = data[data.day == "Monday"]
print(data_monday)
monday_temp = data_monday.temp[0]
temp_fahrenheit = monday_temp * 9 / 5 + 32
print(temp_fahrenheit)

