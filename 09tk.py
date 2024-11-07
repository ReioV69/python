import turtle
import random
# Reio Viikmaa
# 06.11.24

d = 25

for i in range(6):
    c = turtle.pencolor("black")
    # sein
    for i in range(4):
        turtle.fd(d)
        turtle.lt(90)

# uks
    turtle.penup()
    turtle.fd(d*0.25)
    turtle.pendown()
    c = turtle.pencolor("red")
    for i in range(4):
        turtle.fd(d/2)
        turtle.lt(90)


# katus
    turtle.penup()
    turtle.bk(d*0.25)
    turtle.lt(90)
    turtle.fd(d)
    turtle.rt(30)
    turtle.pendown()
    c = turtle.pencolor("lightgreen")
    for i in range(2):
        turtle.fd(d)
        turtle.rt(120)


# järgmine maja
    turtle.penup()
    turtle.fd(d)
    turtle.lt(90)
    turtle.fd(d)
    turtle.lt(90)
    turtle.fd(d+20)
    turtle.pendown()

    d += 5

turtle.done()
