from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

POSITION = (0, 275)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(POSITION)
        self.write(f"Score: {self.score} ",  align=ALIGNMENT,font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ", align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)







