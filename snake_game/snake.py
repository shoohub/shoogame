import time
from turtle import Screen, Turtle

# こちらに定義する理由は、今後の変更を簡単にするため
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Snakeの位置を定義する
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # snakeのパーツをつくる
        for position in STARTING_POSITIONS:
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.segments.append(tim)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):  # 尻尾から移動する
            new_x = self.segments[seg_num-1].xcor()  # 尻尾の一つ前の場所は移動先
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # 北は90

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  # 南

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  # 西

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)  # 東
