from turtle import Turtle

class PongBall(Turtle):
    """Class representing the ball in the Pong game."""

    def __init__(self):
        """Initialize the Pong ball with shape, color, and movement attributes."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_velocity = 10
        self.y_velocity = 10
        self.speed_factor = 0.1

    def move(self):
        """Update the ball's position based on current velocity."""
        new_x = self.xcor() + self.x_velocity
        new_y = self.ycor() + self.y_velocity
        self.goto(new_x, new_y)

    def bounce_off_wall(self):
        """Reverse the ball's vertical direction when it hits the top or bottom walls."""
        self.y_velocity *= -1
        self.speed_factor *= 0.9  # Increase speed slightly on bounce

    def bounce_off_paddle(self):
        """Reverse the ball's horizontal direction when it hits a paddle."""
        self.x_velocity *= -1
        self.speed_factor *= 0.9  # Increase speed slightly on hit

    def reset_position(self):
        """Reset the ball's position and movement speed when a point is scored."""
        self.goto(0, 0)
        self.speed_factor = 0.1
        self.bounce_off_paddle()
