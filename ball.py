from turtle import Turtle

class Ball:
    def __init__(self):
        self.t = Turtle()
        self.t.shape("circle")

        self.t.color("white")
        self.t.penup()
        self.new_x = 10
        self.new_y = 10


    def move(self):
        new_x = self.t.xcor() + self.new_x
        new_y = self.t.ycor() + self.new_y
        self.t.goto(new_x,new_y)

        # self.t.setheading(45)
        # self.t.forward(4)

    def bounce(self):
        self.new_y *= -1

    def bounce_paddle(self):
        self.new_x *= -1

    def reset_pos(self):
        self.t.home()
        self.new_x *= -1
        self.new_y *= -1

    def speed(self):
        self.new_y *= 1.2
        self.new_x *= 1.2

    def reset_speed(self):
        self.new_x = 10
        self.new_y = 10
