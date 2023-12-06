from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from sound import Sound
import time

# Global
ALIGNMENT = "center"
FONT = ("Retro Gaming", 16, "normal")

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Metal Gear Solid Snake")

screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

sound_player = Sound()

# Background music

sound_file = "sound/RaceIntoTheNight.mp3"
sound_player.play_sound(sound_file)


def play_music_again():
    sound_play_again = "sound/RaceIntoTheNight.mp3"
    return sound_player.play_sound(sound_play_again)


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(play_music_again, "space")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #     Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score(1)

    #     Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()
        sound_file = "sound/helicopter.mp3"
        sound_player.play_sound(sound_file)

    #       Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            sound_file = "sound/helicopter.mp3"
            sound_player.play_sound(sound_file)
            scoreboard.game_over()

    

screen.exitonclick()
