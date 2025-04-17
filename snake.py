from turtle import Turtle as Turt
class Snake:

    # def __init__(self,name,cor):
    #     self.name = name
    #     self.cor = cor
    #     self.tur_obj_main = Turt()
    #     self.tur_obj_main.penup()
    #     self.tur_obj_main.shape("square")
    #     self.tur_obj_main.color("white")
    #     self.tur_obj_main.setx(cor)
    #     self.tur_obj_main.shapesize()

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        starting_pos = [(0,0),(-20,0),(-40,0)]
        for pos in starting_pos:
            self.add_segment(pos[0],pos[1])

    def add_segment(self, x , y):
        new_segment = Turt()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.goto(x,y)
        self.segments.append(new_segment)

    def grow(self):
        last_seg = self.segments[-1]
        self.add_segment(last_seg.xcor(), last_seg.ycor())

    def move(self):
        for i in range (len(self.segments) -1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i -1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(20)

    def head(self):
        return self.segments[0]







