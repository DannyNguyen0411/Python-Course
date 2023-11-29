height = input("height in meters: ")
weight = input("weight in kilograms: ")

weight_in_int = int(weight)
height_in_int = float(height)

bmi = float(weight_in_int / (height_in_int * height_in_int))
bmi_result = ("{:.2f}".format(bmi))

print(bmi_result)

