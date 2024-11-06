import turtle
import random
#Reio Viikmaa
#06.11.24
d = 25
for i in range(6):

#sein

 for i in range(4):
    turtle.fd(d)
    turtle.lt(90)
#uks
turtle.penup()
turtle.fd(d*0.25)
turtle.pendown()
for i in range(4):
    turtle.fd(d/2)
    turtle.lt(90)


#katus


#järgmine maja
turtle.penup()
turtle.fd(d+20)
turtle.pendown()


turtle.done()