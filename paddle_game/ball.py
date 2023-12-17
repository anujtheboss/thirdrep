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
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move*=-1
    def bounce_x(self):
        self.x_move*=-1
    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()
        # at this position we start position of x as negative and x_move value also become negative ,so on adding both final value 
        #  of x increase in negative drxn
    
        # now y_move become -10,so when move function is called and when the position is wall ,then the ball go to new x
        # increased by 10 but y is decreased by 10 so the ball go triangualr way
