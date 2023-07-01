from turtle import Turtle, Screen
import random
colors = ["red", "orange", "violet", "indigo", "green", "yellow"]
turtles = []
is_race_on = False


screen = Screen()
screen.setup(width=600, height=400)

bet = screen.textinput(title="enter your bet", prompt="which color is gonna win ? ")


yin = -100
for i in colors:
    tim = Turtle(shape="turtle")
    tim.color(i)
    tim.penup()
    tim.goto(x=-250, y=yin)
    yin += 30
    turtles.append(tim)

if bet:
    is_race_on = True

while is_race_on:
    for i in turtles:
        if i.xcor() > 280 :
            is_race_on = False
            winner  = i.pencolor()
            if winner ==  bet :
                print(f"your won {winner}")
            else :
                print(f"the winner is {winner}")
        dis = random.randint(0, 10)
        i.forward(dis)

screen.exitonclick()