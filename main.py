from turtle import Screen
from snake import Snake
import time
from food import Food
from score import ScoreBoard
screen = Screen()
screen.tracer(0)
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
is_game_on = True

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_refresh()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        score.end_game()
        is_game_on = False

    for segments in snake.segments[1::]:
        if segments.distance(snake.head) < 10:
            is_game_on = False
            score.end_game()


screen.exitonclick()