from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scorboard
import time

is_over = False
s = Screen()
s.setup(600, 600)
s.bgcolor('black')
s.title('Snake Game')
s.tracer(0)

snake = Snake()
food = Food()
sb = Scorboard()
s.listen()
s.onkey(snake.up, 'Up')
s.onkey(snake.down, 'Down')
s.onkey(snake.left, 'Left')
s.onkey(snake.right, 'Right')

while not is_over:
    s.update() 
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) <= 20:
        food.refresh()
        sb.increase_score()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        is_over = True
        sb.game_over()

    for seg in snake.segments:
        if seg == snake.segments[0]:
            pass
        elif snake.segments[0].distance(seg) < 10:
            is_over = True
            sb.game_over()

s.exitonclick()
