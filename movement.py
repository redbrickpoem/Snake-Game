from turtle import Turtle as Turt


class Movement:


    def __init__(self,turtle_obj):
        self.tur_obj = turtle_obj

    def move_up(self):
        if self.tur_obj.heading() != 270:
            self.tur_obj.setheading(90)

    def move_down(self):
        if self.tur_obj.heading() != 90:
            self.tur_obj.setheading(270)

    def move_left(self):
        if self.tur_obj.heading() != 0:
            self.tur_obj.setheading(180)

    def move_right(self):
        if self.tur_obj.heading() != 180:
            self.tur_obj.setheading(0)

    def speed(self,num):
        self.tur_obj.forward(num)

