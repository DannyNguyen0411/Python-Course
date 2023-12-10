import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from sound import Sound

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard.update_score()
sound = Sound()

# This code will make the screen listen
screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    # car_manager.move_cars()

    if player.ycor() > 250:
        print("Congratulations! You reached the next level!")
        scoreboard.increase_score(1)
        car_manager.increase_speed()
        player.next_level()
        # screen.update

    for car in car_manager.all_cars:
        if player.distance(car.xcor(), car.ycor()) < 20:
            print("Game Over!")
            scoreboard.game_over()
            game_is_on = False
            screen.exitonclick()



