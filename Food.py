from turtle import Turtle
import random

class Food:

    def __init__(self):
        self.food = Turtle()
        self.food.penup()
        self.food.color("blue")
        self.food.shape("circle")
        # self.food.shapesize("5")
        self.food.speed("fastest")
        self.food_spawn()

    def food_spawn(self):
        x = random.randint(-13, 13) * 20
        y = random.randint(-13, 13) * 20
        self.food.goto(x,y)

