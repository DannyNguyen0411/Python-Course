from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from sound import Sound
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Metal Gear Solid Snake")

screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

sound_player = Sound()

# # Music for the snake game
# music = Sound()
# sound_track = "sound/RaceIntoTheNight.mp3"
# music.play_sound(sound_track)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.fat_the_snake()
        scoreboard.increase_score(1)
        sound_file = "sound/helicopter.mp3"
        sound_player.play_sound(sound_file)




screen.exitonclick()