from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refesh()

    def refesh(self):
        x_cod = random.randint(-280, 280)
        y_cod = random.randint(-280, 280)

        self.goto(x=x_cod, y=y_cod)