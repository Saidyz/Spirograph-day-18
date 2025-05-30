import turtle as T
import random


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rcolor = ( r, g, b)
    return rcolor


tim = T.Turtle()
T.colormode(255) # this to set the color mode to RBG tuples 'from Turtle docs'


tim.speed(0)

degrees = 10
nm_of = int(360/degrees)
radius = 99
for _ in range(nm_of):
    tim.color(random_color())
    tim.circle(radius)
    tim.right(degrees)



screen = T.Screen()
screen.exitonclick()