from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Midline, PlayerOneScore, PlayertwoScore
import time
right = (350,0)
left = (-350,0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Welcome to Ping Pong Game")

screen.tracer(0)
r_paddle = Paddle(right)
l_paddle = Paddle(left)
ball = Ball()
ball.speed("fastest")
line= Midline()

player1score = PlayerOneScore()
player2score = PlayertwoScore()



screen.listen()

screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    player1score.display_score()
    player2score.display_score()
    ball.move()
    
    #collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with right paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>345:
        ball.bounce_x()
    
        
    
    #collision with left paddle
    if ball.distance(l_paddle)<50 and ball.xcor() <-345:
        ball.bounce_x()
    
    
    #collision with right wall
    if ball.xcor() > 380:
        player2score.update_score()
        ball.recenter()
        

    #collision with left wall
    if ball.xcor() < -380:
        ball.recenter()        
        player1score.update_score()
        # ball.move()

        






screen.exitonclick()
