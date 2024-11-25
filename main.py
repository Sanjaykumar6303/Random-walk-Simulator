from turtle import Turtle,Screen
import random

timmy = Turtle()
colours = ["cyan","dark turquoise","dodger blue","green yellow","blue violet","tomato","dark magenta","antique white"]
# Drawing a random walk
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
timmy.width(10)
# timmy.speed("slowest")
for i in range(100):
    timmy.color(random.choice(colours))
    # timmy.color(random_color())
    timmy.forward(50)
    timmy.setheading(random.choice(directions))

    
screen = Screen()
screen.exitonclick()