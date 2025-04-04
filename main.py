from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("green")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

game_is_on = True
points = 0

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1) #Aqui é onde alteramos o tempo de atualização da tela
    snake.move()
    if snake.head.distance(food) < 15: #Agora iremos detectar a colisão com a comida
        print("nom nom nom")
        points += 1
        score.increase_score()
        food.refresh()

screen.exitonclick()