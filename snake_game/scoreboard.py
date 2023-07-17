from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_game\data.txt", mode="r") as file :
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}",  align="center", font={"Courier", 24, "normal"})


    def reset(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open("snake_game\data.txt", mode="w") as file :
                file.write(f"{self.high_score}")
        self.score = 0
        self.update()


    def game_over(self):
        self.goto(0, 0)
        self.write(f" GAME OVER", align="center", font={"Courier", 24, "normal"})
    


    def increase_score(self):
        self.score += 1
        self.update()