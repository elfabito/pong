from turtle import Screen
from player import Player
from back import Line
from ball import Ball
from score import Score
import time




s = Screen()
s.tracer(0)

line = Line()
player_1 = Player((-350,0))
player_2 = Player((350,0))
score_1 = Score((-70,200))
score_2 = Score((70,200))

b = Ball()

s.setup(height=600, width=800)
s.bgcolor("Black")
s.listen()
s.onkey(player_1.move_up, "Up")
s.onkey(player_1.move_down, "Down")
s.onkey(player_2.move_up, "w")
s.onkey(player_2.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()


    b.move()
    if b.t.ycor() > 280 or b.t.ycor() < - 280:
        b.bounce()

    if (b.t.distance(player_2) < 62 and b.t.xcor() > 320 and b.t.xcor() < 340) or (b.t.distance(player_1) < 62 and  b.t.xcor() < -320 and b.t.xcor() > -340):
        b.bounce_paddle()
        b.speed()

    elif b.t.xcor() > 380:
        score_1.raise_score()
        b.reset_speed()
        b.reset_pos()

    elif b.t.xcor() < -380:
        score_2.raise_score()
        b.reset_speed()
        b.reset_pos()
        b.reset_pos()





s.exitonclick()
