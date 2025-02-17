from turtle import Turtle

class Scoreboard(Turtle):
    """Handles the scoreboard display for the Pong game."""

    def __init__(self):
        """Initialize the scoreboard with default settings."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Refresh the scoreboard display with the current scores."""
        self.clear()
        self.goto(-100, 190)
        self.write(self.left_score, align="center", font=("Times New Roman", 80, "normal"))
        self.goto(100, 190)
        self.write(self.right_score, align="center", font=("Times New Roman", 80, "normal"))

    def increase_left_score(self):
        """Increase the left player's score and update the scoreboard."""
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        """Increase the right player's score and update the scoreboard."""
        self.right_score += 1
        self.update_scoreboard()
