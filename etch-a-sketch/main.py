from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_left():
    t.setheading(t.heading() + 10)

def turn_right():
    t.setheading(t.heading() - 10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()
s.onkey(move_forwards, "w")
s.onkey(move_backwards, "s")
s.onkey(turn_right, "d")
s.onkey(turn_left, "a")
s.onkey(clear, "c")
s.exitonclick()
