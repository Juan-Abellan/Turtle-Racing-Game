# TODO: IMPORTS
from turtle import Turtle, Screen
from random import randint

# TODO: FUNCTIONS


# TODO: ----------------------------------------------------------------------------------------------------------------
# TURTLES STARTING CONDITIONS
turtle_colors = ["red", "green", "blue", "black", "yellow", "orange", "grey"]
turtles_positions = [-150, -100, -50, 0, 50, 100, 150, 200]
turtle_list = []

# SCREEN SET UP
screen = Screen()
screen.setup(width=500, height=400)

# TURTLES DISPLAY
for index in range(0, len(turtle_colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(turtle_colors[index])
    turtle.penup()
    turtle.goto(x=-230, y=turtles_positions[index])
    turtle_list.append(turtle)

# USER
user_bet = screen.textinput(title="bet time",
                            prompt="Which turtle will win?\nred, green, blue, black, yellow, orange, grey"
                            ).lower()

# RACING
if user_bet:
    racing = True

    while racing:
        for turtle in turtle_list:
            if turtle.xcor() > 230:
                racing = False
                color_winner = turtle.pencolor()
                if user_bet == color_winner:
                    print(f"The winner turtle is {user_bet}, good job!")
                else:
                    print(f"The winner turtle is {color_winner}, you lost!")

            random_distance = randint(0, 10)
            turtle.fd(random_distance)

screen.exitonclick()
