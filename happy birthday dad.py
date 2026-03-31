import turtle
import random
import math

# Set up the screen
t = turtle.Turtle()
turtle.bgcolor("lightblue")
turtle.title("Happy Birthday Dad!")
t.speed(0)
t.pensize(3)

# Function to draw heart
def heart():
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()
    t.setheading(0)

# Draw heart first
heart()

# Write “37” inside the heart
t.penup()
t.goto(0, -40)
t.color("white")
t.pendown()
t.write("36", align="center", font=("Comic Sans MS", 60, "bold"))

# Function to draw a balloon
def balloon(color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.color("black")
    t.right(90)
    t.forward(60)
    t.left(90)

# Balloons
balloon("deeppink", -180, 100)   # slightly left-shifted pink balloon
balloon("yellow", 0, 150)
balloon("green", 150, 100)

# Curly foil curtains (with increased boldness)
def random_curly_foil_curtains():
    colors = ["gold", "silver", "hotpink", "cyan", "violet", "lightgreen"]
    for x in range(-300, 300, 25):
        t.penup()
        t.goto(x, 250)
        t.pendown()
        t.color(random.choice(colors))
        # Increased minimum thickness for bolder ribbons
        t.pensize(random.randint(3, 6))
        amplitude = random.randint(4, 9)     # curliness
        length = random.randint(70, 150)     # height
        t.setheading(-90)
        for i in range(length // 3):
            y = 250 - i * 3
            dx = math.sin(i / 2) * amplitude
            t.goto(x + dx, y)
        t.penup()
    
    # Glitter dots for sparkle
    for i in range(60):
        t.goto(random.randint(-300, 300), random.randint(230, 270))
        t.dot(random.randint(6, 14), random.choice(colors))

# Draw foil curtains
random_curly_foil_curtains()

# Main text messages
t.penup()
t.goto(-230, -50)
t.color("purple")
t.pendown()
t.write("🎉 Happy Birthday Dad! 🎉", font=("Comic Sans MS", 28, "bold"))

t.penup()
t.goto(-100, -100)
t.color("darkblue")
t.pendown()
t.write("Love You Dad", font=("Harlow Solid Italic", 28, "bold"))

# Hide turtle
t.hideturtle()
turtle.done()
