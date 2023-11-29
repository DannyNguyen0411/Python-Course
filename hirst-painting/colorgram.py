import colorgram
import random

colors = colorgram.extract('image.jpg', 30)

rgb_colors = []

print("Method 1:")
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)