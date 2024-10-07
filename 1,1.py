import turtle
# Reio Viikmaa
# 04.10.24
# Harjutus 01 Kilpkonn
# muudan asukohta
turtle.speed(10)
turtle.penup()
turtle.goto(-500,300)
turtle.pendown()
#kolmnurk
turtle.color("yellow")
turtle.fd(200)
turtle.left(120)
turtle.fd(200)
turtle.left(120)
turtle.fd(200)
turtle.left(120)

turtle.penup()
turtle.goto(-250,200)
turtle.pendown()


#nimi esitäht
turtle.color("red")
turtle.fd(30)
turtle.left(90)
turtle.fd(60)
turtle.right(135)
turtle.fd(90)
turtle.left(45)
turtle.fd(30)
turtle.left(135)
turtle.fd(90)
turtle.right(90)
turtle.circle(60,150)
turtle.lt(75)
turtle.fd(160)
turtle.lt(90)
turtle.penup()
turtle.fd(20)
turtle.lt(90)
turtle.fd(70)
turtle.rt(90)
turtle.pendown()


turtle.circle(32,180)
turtle.lt(90)
turtle.fd(65)
turtle.penup()




#võlv nr 8
turtle.color("blue")

turtle.penup()
turtle.goto(-150,400)
turtle.pendown()

turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.circle(50,180)

# Lõpetan, et ei jookseks kokku
turtle.done()