from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.title("pong")
screen.bgcolor("black")
screen.tracer(0)
# putting 0 turn off the animation

l_paddle=Paddle((-350,0))
# on creating object init function automatically get called
r_paddle=Paddle((350,0))

ball=Ball()
scoreboard=Scoreboard()
screen.listen()  
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detecting collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        # width of the ball is 20px
        # need to bounce
        ball.bounce_y()
    # detect collision with right paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
# detect when right paddle misses the ball
    if ball.xcor()>380:
        ball.reset_ball()
        scoreboard.l_point()
        # detect when left paddle misses
    if ball.xcor()<-380:
        ball.reset_ball()
        scoreboard.r_point()

    # as the animation gets off due to tracer attribute ,all the activities from tracer upto update attribute are hidden
    # then when screen.update is used the paddle directly appear  in required position .so not showing moving of paddle from default position


screen.exitonclick()