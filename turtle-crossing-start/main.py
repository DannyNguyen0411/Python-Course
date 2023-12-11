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
sound_play = "sound/MarioMetalCap.mp3"
sound.play_sound(sound_play)

# This code will make the screen listen
screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")
screen.onkey(player.easter_egg, "q")

# Boosters
screen.onkey(player.speed_off, "a")

power_booster = 5

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # if screen.onkey(player.speed_off, "a") and power_booster > 0:
    #     player.speed_off()
    #     scoreboard.decrease_booster(1)
    #     print(power_booster)
    #     power_booster -= 1
    # elif power_booster == 0:
    #     print("No boosters left!")

    if player.ycor() > 250:
        print("Congratulations! You reached the next level!")
        scoreboard.increase_score(1)
        player.next_level()
        car_manager.increase_speed()

        # screen.update

    for car in car_manager.all_cars:
        if player.distance(car.xcor(), car.ycor()) < 20:
            print("Game Over!")
            sound_game_over = "sound/TokyoDrift.mp3"
            sound.play_sound(sound_game_over)
            scoreboard.game_over()
            game_is_on = False
            screen.exitonclick()
