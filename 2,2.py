import turtle
#Reio Viikmaa 07.10.24
#Harjutus 2
aken = turtle.Screen()
aken.setup(width = 500, height= 400)
aken.title("Sinilill - Reio")
turtle.speed("fastest")
turtle.pensize(10)

#sinilill
turtle.pencolor("green")
turtle.goto(0,-150)
turtle.lt(90)
turtle.fd(200)
turtle.lt(-90)
turtle.begin_fill()
turtle.color("blue", "light blue")
turtle.circle(70)
turtle.lt(90)
turtle.fd(50)
turtle.end_fill()
turtle.begin_fill()
turtle.color("yellow", "yellow")
turtle.fd(50)
turtle.end_fill()



turtle.done()
