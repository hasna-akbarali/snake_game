from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open('../../Desktop/high_score.txt', 'r') as f:
            self.high_score = int(f.read())
        self.goto(0, 260)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score : {self.score} High Score : {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('/Users/DELL/Desktop/high_score.txt', 'w') as f:
                f.write(f'{self.high_score}')
        self.score = 0
        self.update_score()

    def increment(self):
        self.score += 1
        self.update_score()
