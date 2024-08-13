from turtle import Turtle, Screen
import random
is_race_on = False

s = Screen()
s.setup(500, 400)
bet = s.textinput("Make a bet", "Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [-75, -45, -15, 15, 45, 75]
turtles = []
winner = ""

for index in range(0, 6):
    t = Turtle()
    t.penup()
    t.color(colors[index])
    t.shape("turtle")
    t.goto(-225, y_coordinates[index])
    turtles.append(t)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 225:
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You're won! The {winner} turtle won the race.")
            else:
                print(f"Your lost. The {winner} turtle won the race.")
            is_race_on = False
            break
        turtle.forward(random.randint(0, 10))

s.exitonclick()
