import turtle
import colorsys
t = turtle.Turtle()

t.speed(1)
turtle.bgcolor('black')
c = colorsys.hsv_to_rgb(70, 1, 1)
t.color(c)
t.pensize(1)

for i in range(100):
    t.fd(100)
    t.right(45)
    t.fd(100)
    t.right(45)
    t.fd(100)

t.hideturtle()
turtle.done()