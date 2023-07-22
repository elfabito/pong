from turtle import Turtle
MOVE_DIS = 10

class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position

        self.create_player()

    def move_down(self):

        self.backward(20)

    def move_up(self):
        self.forward(20)

    def create_player(self):

        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(self.position)
        self.turtlesize(stretch_wid=1, stretch_len=5)



