from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

POSITION = (0, 275)


def set_highscore():
    file = open("data.txt")
    content = file.read()
    return content


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = set_highscore()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(POSITION)
        self.write(f"Score: {self.score} High Score: {self.highscore}",  align=ALIGNMENT,font=FONT)

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",  align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()








