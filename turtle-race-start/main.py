from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
color = ['red', 'green', 'yellow', 'blue', 'orange', 'purple']
screen.colormode(255)
player_bet = screen.textinput("Turtle race", "Which turtle will win?")


all_turtles = []

for index in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.color(color[index])
    tim.penup()
    tim.goto(x=-230, y=-150 + 50 * index)
    all_turtles.append(tim)

x = True
while x:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            x = False
            print(f"{turtle.pencolor().title()} turtle won the race.")
            if  player_bet == turtle.pencolor():
                print('You win.')
            else:
                print('You lose.')







screen.exitonclick()