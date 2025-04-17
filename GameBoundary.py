from turtle import Turtle as Turt

class GameBoundary:

    def __init__(self):
        self.tur_obj_bound = Turt()
        self.tur_obj_bound.penup()
        self.tur_obj_bound.color("green")
        self.tur_obj_bound.shape("turtle")
        self.tur_obj_bound.hideturtle()
        self.tur_obj_bound.goto(-295,295)

    def draw_boundary(self):
        self.tur_obj_bound.color("white")
        self.tur_obj_bound.pensize(10)
        self.tur_obj_bound.pendown()
        for i in range(0, 2):
            self.tur_obj_bound.forward(580)
            self.tur_obj_bound.right(90)
            self.tur_obj_bound.forward(570)
            self.tur_obj_bound.right(90)

    def boundary_coll(self, snake_head):
        x = snake_head.xcor()
        y = snake_head.ycor()

        if x > 270 or x < -270 or y > 260 or y < -260:
            return True
        return False
