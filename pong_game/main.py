import random
import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

# 画面を定義する
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("SHOO's pong game")
screen.tracer(0)

# 板を作る
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# ボールを作る
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

scoreboard = Scoreboard()

game_is_go = True
while game_is_go:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision with ball
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect  R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
