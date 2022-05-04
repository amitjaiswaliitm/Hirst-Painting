from turtle import Turtle
FONT = ("Arial", 10, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()


