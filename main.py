#Creation of board of the game
from turtle import Screen
from snake import Snake
import time
#Creation of the board
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake game")
screen.tracer(0)
snake = Snake()
#Snake animation
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.5)
    snake.move()

screen.exitonclick()