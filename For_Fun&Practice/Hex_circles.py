import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
colors = ["red", "green", "blue", "yellow", "cyan", "purple", "violet"]
for i in range(200):
    t.pencolor(colors[i % 7])
    t.circle(i * 1.5)
    t.right(300)
    t.forward(300)
turtle.done()