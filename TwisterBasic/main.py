import random

# Todo. Make a list for body parts and colors

colors = ("red", "blue", "green", "yellow")
limbs = ("left hand", "right hand", "left foot", "right foot")

color_random = random.choice(colors)
limbs_random = random.choice(limbs)
print(f"{color_random}, {limbs_random}")