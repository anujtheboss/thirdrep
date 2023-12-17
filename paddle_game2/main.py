from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.title("pong game")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)
l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))

ball=Ball()
screen.listen()
scoreboard=Scoreboard()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



is_game_on=True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    # detect collision with right paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    # detect if paddle misses the ball
    if ball.xcor()>380:
        ball.reset_ball()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.reset_ball()
        scoreboard.r_point()
screen.exitonclick()