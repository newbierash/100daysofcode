from turtle import Screen
from snake import Snake
import time

is_over = False
s = Screen()
s.setup(600, 600)
s.bgcolor('black')
s.title('Snake Game')
s.tracer(0)

snake = Snake()
s.listen()
s.onkey(snake.up, 'Up')
s.onkey(snake.down, 'Down')
s.onkey(snake.left, 'Left')
s.onkey(snake.right, 'Right')

while not is_over:
    s.update() 
    time.sleep(0.1)
    snake.move()

s.exitonclick()
