import time
from turtle import Screen, Turtle

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SHOO Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:  # Snakeが進行させるループ処理
    screen.update()  # Snakeが移動完了後に表示させる、でないと、繋いてないように見える
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
