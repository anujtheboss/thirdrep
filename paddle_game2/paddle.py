from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=3)
        self.penup()
        self.goto(position)
    def go_up(self):
        self.goto(self.xcor(),self.ycor()+10)
    def go_down(self):
        self.goto(self.xcor(),self.ycor()-10)
   