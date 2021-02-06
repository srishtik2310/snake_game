from turtle import Turtle
ALIGNMENT_SCORE = "right"
FONT_SCORE = ("skia", 20, "normal")
ALIGNMENT_END = "center"
FONT_END = ("skia", 54, "bold")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(290, 280)
        self.score = 0
        self.write(arg= f"Score: {self.score} ", align = ALIGNMENT_SCORE, font = FONT_SCORE)
    def score_refresh(self):
        self.clear()
        self.score += 1
        self.write(arg= f"Score: {self.score} ", align=ALIGNMENT_SCORE, font = FONT_SCORE)

    def end_game(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER !!", align = ALIGNMENT_END, font = FONT_END)
