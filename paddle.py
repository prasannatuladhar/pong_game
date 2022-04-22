from turtle import Turtle,Screen


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setpos(position)
        self.shapesize(stretch_wid=5,stretch_len=1)
        

    def move_up(self):
        y_pos = self.ycor() + 40
        x_pos = self.xcor()
        self.goto(x_pos,y_pos)
    
    def move_down(self):
        y_pos = self.ycor() - 40
        x_pos = self.xcor()
        self.goto(x_pos,y_pos)