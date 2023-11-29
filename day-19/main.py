from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.pensize(10)

def move_forwards():
    tim.forward(10)


def back_forwards():
    tim.backward(10)


def clockwise():
    # # Method 1
    # tim.right(10)

    # Method 2
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def counter_clockwise():
    # # Method 1
    # tim.left(10)

    # Method 2
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear_screen():
    tim.home()
    screen.resetscreen()


screen.listen()


def controllers():
    screen.onkey(move_forwards, "w")
    screen.onkey(back_forwards, "s")
    screen.onkey(clockwise, "d")
    screen.onkey(counter_clockwise, "a")
    screen.onkey(clear_screen, "c")
    return True


controllers()

screen.exitonclick()
