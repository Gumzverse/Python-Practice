import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Flappy Bird Game")
screen.bgcolor("sky blue")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the bird
bird = turtle.Turtle()
bird.shape("triangle")
bird.color("yellow")
bird.penup()
bird.speed(0)
bird.goto(-200, 0)
bird.dy = 0

# Gravity
gravity = -0.2

# Create the pipes
pipes = []

# Score
score = 0

# Create the score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Functions to control the bird
def jump():
    bird.dy = 5

# Functions to create pipes
def create_pipe(x, y):
    pipe = turtle.Turtle()
    pipe.shape("square")
    pipe.color("green")
    pipe.shapesize(stretch_wid=10, stretch_len=2)
    pipe.penup()
    pipe.speed(0)
    pipe.goto(x, y)
    pipes.append(pipe)

# Keyboard bindings
screen.listen()
screen.onkeypress(jump, "space")

# Main game loop
while True:
    screen.update()

    bird.dy += gravity
    bird.sety(bird.ycor() + bird.dy)

    # Check for collision with the ground
    if bird.ycor() < -280:
        bird.goto(-200, 0)
        bird.dy = 0

    # Move the pipes
    for pipe in pipes:
        pipe.setx(pipe.xcor() - 2)

        # Check for collision with the bird
        if pipe.distance(bird) < 20 and abs(pipe.xcor() - bird.xcor()) < 20:
            score = 0
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        # Check if pipe is out of screen
        if pipe.xcor() < -400:
            pipe.hideturtle()
            pipes.remove(pipe)
            score += 1
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Create new pipes
    if len(pipes) == 0 or pipes[-1].xcor() < 200:
        create_pipe(400, 200)

    time.sleep(0.03)
