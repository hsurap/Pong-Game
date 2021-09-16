from turtle import Screen
from paddle import Paddle
from  scoreboard import ScoreBoard
from ball import Ball
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(False)

l_paddle=Paddle(-350,0)
r_paddle=Paddle(350,0)
screen.tracer(True)
ball=Ball()
scoreboard=ScoreBoard()
screen.tracer(False)

game_is_on=True

screen.listen()
screen.onkey(fun=r_paddle.up,key="Up")
screen.onkey(fun=r_paddle.down,key="Down")
screen.onkey(fun=l_paddle.up,key="w")
screen.onkey(fun=l_paddle.down,key="s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320:
        ball.bounce_x()

    if ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()