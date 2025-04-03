from turtle import Screen,Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("green")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    #Aqui é onde alteramos o tempo de atualização da tela
    time.sleep(0.30)
    print("hello world")

    snake.move()

screen.exitonclick()