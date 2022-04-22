from turtle import Turtle,Screen
import random

rand_location = random.randint(-280,280)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_move=10
        self.y_move=10
        self.ball_speed = 0.1
     

    def move(self):
        self.penup()
        x_distance = self.xcor()+self.x_move
        y_distance = self.ycor()+self.y_move
        self.goto(x_distance,y_distance)   

    def bounce_y(self):
        self.y_move *= -1   
        

    def bounce_x(self):
        self.x_move *= -1 
        self.ball_speed *=0.9  
    

    def recenter(self):
        self.goto(0,0)  
        self.ball_speed = 0.1
