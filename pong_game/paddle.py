from turtle import Screen, Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # 板を定義する
        self.color("white")
        self.shape("square")
        # defaultは20*20、ここでは倍数を設定する
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        screen = Screen()

    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)
