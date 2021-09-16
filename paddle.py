from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(x=x_cor, y=y_cor)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


