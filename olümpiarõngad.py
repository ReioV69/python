import turtle
#Reio Viikmaa 07.10.24
#Harjutus 2
aken = turtle.Screen()
aken.setup(width = 500, height= 400)
aken.title("Olümpiarõngad")
turtle.speed(0)
turtle.pensize(6)

#olümpiarõngad
turtle.penup()
turtle.goto(-120,-20)
turtle.pendown()
turtle.color("blue")
turtle.circle(50)

#kollane
turtle.penup()
turtle.goto(-60,-60)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)


# punane
turtle.penup()
turtle.goto(120,-20)
turtle.pendown()
turtle.color("red")
turtle.circle(50)

# roheline
turtle.penup()
turtle.goto(60,-60)
turtle.pendown()
turtle.color("green")
turtle.circle(50)
# must
turtle.penup()
turtle.goto(0,-20)
turtle.pendown()
turtle.color("black")
turtle.circle(50)



turtle.done()
