
"""A primeira coisa que queremos fazer aqui, é que a classe food herde da classe turtle.
   Dessa forma nossa classe food terá todos os recursos da classe turtle, mas também
   terá algumas coisas especificas que diremos a ela como fazer, para que se comporte
   como um alimento"""
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        """Daqui em diante podemos começar a usar coisas que pertencem à classe turtle"""
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("purple")
        self.speed("fastest") #Para não ver o alimento sendo criado e movido pela tela
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  # Para especificar a coordenada onde desejo colocar o alimento

