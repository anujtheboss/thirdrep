from turtle import Turtle
STARTING_POSITONS=[(0,0),(-20,0),(-40,0)]
# in python all the constant are written in capital
# in python class are written in pascal case
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        # here head is assigned with something ,self. is alse necessary to use,while using this value in main progrm
        # use object.head
    def create_snake(self):
        for position in STARTING_POSITONS :
            self.add_segment(position)
            # new_segment=Turtle("square")
            # new_segment.color("white")
            # new_segment.penup()
            # new_segment.goto(position)
            # self.segments.append(new_segment)
    def add_segment(self,position):
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    def extend(self):
            self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[segment_num-1].xcor()
            new_y=self.segments[segment_num-1].ycor()
            self.segments[segment_num].goto(new_x,new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
     if self.head.heading()!=UP:
        self.head.setheading(DOWN)
    def left(self):
     if self.head.heading()!=RIGHT:
        self.head.setheading(LEFT)
    def right(self):
     if self.head.heading()!=LEFT:
        self.head.setheading(RIGHT)