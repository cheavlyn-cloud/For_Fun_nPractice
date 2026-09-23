import turtle
import random
import math

#Setup Screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Galaxy Simulation with Turtle Graphics")
screen.tracer(0) #Turn off automatic updating

#Create stars
num_stars = 100
stars = []

for i in range(num_stars):
    star = turtle.Turtle()
    star.shape("circle")
    star.color(random.random(), random.random(),random.random())
    star.penup()
    star.speed(0)
    #Random distance and angle from center
    distance = random.randint(50,300)
    angle = random.randint(0, 360)
    star.goto(distance * math.cos(math.radians(angle)))
    star.dist = distance
    star.angle = angle 
    star.speed_factor = random.uniform(0.5,2)
#Individual rotation speed
    stars.append(star)

    #Animate stars
while True:
    for star in stars:
        #Update angle
        star.angle += star.speed_factor
        #Move star around the center
        x = star.dist * math.cos(math.radians(star.angle))
        y = star.dist * math.sin(math.radians(star.angle))
        star.goto(x, y)
        #Twinkle effect
        star.shapesize(random.uniform(0.5, 1.5))
        star.color(random.random(), random.random(), random.random())
    screen.update()