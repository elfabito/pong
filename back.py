from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.pensize(2)
        self.create_line()
    def create_line(self):
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)




# t = Turtle()
# t.color("white")
# t.penup()
# t.goto(0,-280)
# t.setheading(90)
# t.pensize(2)
# def move():
#     for _ in range(30):
#         t.pendown()
#         t.forward(10)
#         t.penup()
#         t.forward(10)
#
# move()
