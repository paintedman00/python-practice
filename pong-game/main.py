from turtle import Screen
from paddle import Paddle
from ball import PongBall
from scoreboard import Scoreboard
import time

# Set up the game screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)  # Turns off automatic updates for smooth animation

# Create game objects
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = PongBall()
scoreboard = Scoreboard()

# Set up key controls
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

# Start the game loop
game_active = True
while game_active:
    time.sleep(ball.speed_factor)  # Adjust speed dynamically
    screen.update()
    ball.move()

    # Ball collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_off_wall()

    # Ball collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_off_paddle()

    # Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Close the game on click
screen.exitonclick()
