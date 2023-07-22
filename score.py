from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 70, "bold")
class Score:
    def __init__(self, position):
        self.position = position
        self.t = Turtle()
        self.score = 0
        self.t.penup()
        self.t.color("white")
        self.t.hideturtle()
        self.t.shapesize(4)
        self.t.goto(position)
        self.update_score()
    def update_score(self):
        self.t.write(f"{self.score}", True, align=ALIGNMENT, font=FONT)
    def raise_score(self):
        self.t.clear()
        self.t.goto(self.position)
        self.score += 1
        self.update_score()