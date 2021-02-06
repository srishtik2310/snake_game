from turtle import Turtle
POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in POS:
            self.add_segment(i)


    def add_segment(self, pos):
        s = Turtle(shape = "square")
        s.color("white")
        s.penup()
        s.goto(pos)
        self.segments.append(s)

    def extend(self):
        cordinate = self.segments[-1].position()
        self.add_segment(cordinate)

    def move_forward(self):
        for k in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[k - 1].xcor()
            new_y = self.segments[k - 1].ycor()
            self.segments[k].goto(x = new_x, y = new_y)
        self.segments[0].forward(20)



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)








