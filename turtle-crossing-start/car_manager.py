from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# included it by myself
STARTING_POSITIONS = [(0, 0), (-20, 0)]

class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        random_chance = random.randint(1, 2)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    # def __init__(self):
    #     self.cars = []
    #     self.build_car()
    #     # self.head = self.cars[0]
    #
    #
    # def build_car(self):
    #     for position in STARTING_POSITIONS:
    #         self.add_car(position)
    #
    #
    # def add_car(self, position):
    #     new_car = Turtle()
    #     new_car.shape('square')
    #     new_car.color(random.choice(COLORS))
    #     new_car.penup()
    #     new_car.shapesize(1)
    #     new_car.setheading(180)
    #     new_car.goto(position)
    #
    # def move(self):
    #     for car in self.cars:
    #         car.forward(MOVE_INCREMENT)
