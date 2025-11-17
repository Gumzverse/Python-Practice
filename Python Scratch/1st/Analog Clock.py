import turtle
import time

# Create a turtle screen
screen = turtle.Screen()
screen.title("Analog Clock")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the clock face
clock = turtle.Turtle()
clock.speed(0)
clock.color("white")
clock.width(7)
clock.penup()
clock.goto(0, -200)
clock.pendown()
clock.circle(200)

# Create the hour, minute, and second hands
hour_hand = turtle.Turtle()
hour_hand.speed(0)
hour_hand.color("white")
hour_hand.width(4)
hour_hand.shape("arrow")
hour_hand.shapesize(stretch_wid=0.8, stretch_len=12)
hour_hand.setheading(90)

minute_hand = turtle.Turtle()
minute_hand.speed(0)
minute_hand.color("white")
minute_hand.width(3)
minute_hand.shape("arrow")
minute_hand.shapesize(stretch_wid=0.6, stretch_len=18)
minute_hand.setheading(90)

second_hand = turtle.Turtle()
second_hand.speed(0)
second_hand.color("red")
second_hand.width(2)
second_hand.shape("arrow")
second_hand.shapesize(stretch_wid=0.4, stretch_len=25)
second_hand.setheading(90)

def draw_clock(h, m, s):
    # Draw the hour hand
    hour_angle = (h / 12) * 360 + (m / 60) * 30
    hour_hand.setheading(-hour_angle)
    hour_hand.penup()
    hour_hand.goto(0, 0)
    hour_hand.pendown()
    hour_hand.forward(80)

    # Draw the minute hand
    minute_angle = (m / 60) * 360
    minute_hand.setheading(-minute_angle)
    minute_hand.penup()
    minute_hand.goto(0, 0)
    minute_hand.pendown()
    minute_hand.forward(120)

    # Draw the second hand
    second_angle = (s / 60) * 360
    second_hand.setheading(-second_angle)
    second_hand.penup()
    second_hand.goto(0, 0)
    second_hand.pendown()
    second_hand.forward(140)

def update_clock():
    # Get the current time
    current_time = time.localtime()
    h = current_time.tm_hour % 12
    m = current_time.tm_min
    s = current_time.tm_sec

    draw_clock(h, m, s)

    screen.update()
    screen.ontimer(update_clock, 1000)

update_clock()

turtle.done()