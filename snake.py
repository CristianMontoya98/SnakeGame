from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
class Snake:
    #constructor
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    #Creation of the snake Method
    def create_snake(self):
        #Create the body of the snake
        #Snake segments
        for i in STARTING_POSITION:
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(i)
            self.snake_body.append(snake_segment)

    def move(self):
        for i in range (len(self.snake_body)-1,0,-1):
                x = self.snake_body[i - 1].xcor()
                y = self.snake_body[i - 1].ycor()
                self.snake_body[i].goto(x,y)
        self.snake_body[0].forward(20)