from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10
    def move(self):
        new_x=self.xcor()+self.x_move
        print(new_x)
        new_y=self.ycor()+self.y_move
        print(new_y)
        self.goto(new_x,new_y) 
    def bounce_y(self):
        self.y_move*=-1
    def bounce_x(self):
        self.x_move*=-1
    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()