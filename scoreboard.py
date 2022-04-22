from turtle import Turtle,Screen


class Midline(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=29,stretch_len=0.1)

class PlayerOneScore(Turtle):
    def __init__(self):
        super().__init__()
        self.score =1
   
        self.color("white")
        self.penup()
        self.goto(150,230)  
        self.score = 0

    def display_score(self):
        self.clear()
        self.write(f"{self.score}",align="center",font=("Arial", 50, "normal"))  
        self.hideturtle() 

    def update_score(self):
        self.score +=1    

class PlayertwoScore(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-150,230)  
        self.score = 0
        
    def display_score(self):
        self.clear()
        self.write(f"{self.score}",align="center",font=("Arial", 50, "normal"))  
        self.hideturtle()  

    def update_score(self):
        self.score +=1   
       