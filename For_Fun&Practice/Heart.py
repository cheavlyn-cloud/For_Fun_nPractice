#Heart shape
import turtle

turtle.speed(115)
turtle.bgcolor('black')
turtle.pensize(3)
turtle.color('red', 'pink')
turtle.begin_fill()

# Start drawing the heart
turtle.left(140)
turtle.forward(111.65)

# Left curve
for i in range(200):
    turtle.right(1)
    turtle.forward(1)

turtle.left(120)

# Right curve
for i in range(200):
    turtle.right(1)
    turtle.forward(1)

turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done()