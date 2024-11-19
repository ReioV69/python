# Reio Viikmaa 19.11.24
# Ülesanne 13


import turtle

screen = turtle.Screen()
t = turtle.Turtle()
 
# Küsi kasutajalt numbrilist sisendit
pikkus = screen.numinput("Vanuse sisestamine", "Joonlaua pikksu", default=20, minval=0, maxval=100)
vanus = 8
cm = 10
mm = 3
t.speed(0)

for i in range(int(pikkus)):
    for j in range(10):
        t.fd(mm)
        t.lt(90)
        t.fd(mm)
        t.lt(180)
        t.fd(mm)
        t.lt(90)
    t.lt(90)
    t.fd(cm)
    t.write(i+1,font=("Arial",8, "normal"))
    t.lt(180)
    t.fd(cm)
    t.lt(90)       
    
turtle.done()