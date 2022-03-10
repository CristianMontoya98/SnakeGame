
from turtle import Turtle
class ScoreBoard(Turtle):
    FONT = ('Verdana', 30, 'bold')
    ALIGN = 'left'
    points = 0
    def __init__ (self):
        
        super().__init__()
        self.penup()
        self.goto((-295,260))
        
        self.showPoints()
        

    #Method to draw the points using turtle.write
    def showPoints (self):
        self.color("black")
        self.write(f"POINTS: {self.points}", False, align=self.ALIGN, font = self.FONT)
        self.hideturtle()
    #Method to increment the points
    def increase_points(self):
        self.clear()
        self.points += 1
        self.showPoints()
    
    def game_over(self):
        self.clear()
        self.write("GAME OVER", False, align=self.ALIGN, font = self.FONT)