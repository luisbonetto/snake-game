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
    # Aqui é onde alteramos o tempo de atualização da tela
    time.sleep(0.1)
    snake.move()
    # Detecta colisão com a comida
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend_segment()
        score.increase_score()

    #Detecta colisão com a parede
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    #Detecta colisão com o corpo
    # for segment in snake.segments:
    #     #Descontamos a cabeça
    #     if segment == snake.head:
    #         pass
    #     #Começamos a contar a partir do corpo
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score.game_over()

    #‘Loop’ for atualizado com 'Slice', ou seja, fatíamos a nossa fila depois do índice 0
    # Em seguida começamos contar a partir do índice 1
    for segment in snake.segments[1:]:
        #Começamos a contar a partir do corpo
        if snake.head.distance(segment) <  10:
            game_is_on = False
            score.game_over()

screen.exitonclick()