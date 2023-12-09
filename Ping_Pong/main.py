from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from sound import Sound
from scoreboard import Scoreboard
import time


# For the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)


sound = Sound()

# background music

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()


# music
sound_background = "sound/deathGlamour.mp3"
sound.play_sound(sound_background)
def helicopter():
    sound_file = "sound/helicopter.mp3"
    sound.play_sound(sound_file)

screen.listen()
# screen.onkey(helicopter, 'space')

# Left paddle
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# Right paddle
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    sound_test = "sound/RaceIntoTheNight.mp3"
    sound_test2 = "sound/RaceIntoTheNight.mp3"
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        print("Test")
        ball.bounce_y()

#     Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("Made in China")
        ball.bounce_x()
        ball.speed_up()
        print(ball.speed_up())
        # sound.play_sound(sound_test)

    #     Detect right paddle or left paddle misses
    if ball.xcor() > 380:
        print("Left wins!")
        ball.refresh_speed()
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        print("Right wins!")
        ball.refresh_speed()
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()

