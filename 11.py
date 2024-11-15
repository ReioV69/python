import turtle
import random
# Reio Viikmaa
#15.11.24
# Ülesanne 11

# def tervita(a):
#     print("tere "+a)

# tervita("Mario")




def pikim_sona(a):
    pikimSona = 0
    for sona in a: 
        if len(sona)>pikimSona:
            pikimSona = len(sona)
    print(pikimSona) 
    	
sonad = ["üks", "kaks", "kolm", "kuusteist", "viis", "sadakuuskümmend"]

pikim_sona(sonad)

#Kirjuta funktsioon nimega kolm_pikimat_sona(), mis analüüsib sõnade listi ja leiab kolm kõige pikemat sõna. Lisa kontroll juhuks, kui sõnade arv pole piisav.

def kolm_pikimat_sona(a):
    uusSonastik = {}
    for sona in a:
        uusSonastik[sona] = len(sona)
    jar = (sorted(uusSonastik.items(), key=lambda x:x[1], reverse=True))
    if len(a)<3:
        print("Sõnade arv pole piisav")
    else:
        for i in range(3 ):
            print(jar[i][0])

kolm_pikimat_sona(sonad)







def sarnased_esitahed(a):
    tykk = a.split(" ")
    if tykk[0][0].lower()==(tykk[1][0]).lower():
        return "True"
    else:
        return "False"

print(sarnased_esitahed('Vapper Vares'))
print(sarnased_esitahed('Lahe Känguru'))




# Kilpkonn – kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5

print("------------- Joonistame kujundeid -----------------")
print("Vali kujund: \n1 viinurk \n2 ring \n3 ruut \n4 suvaline")
kujund = (int(input("Sisesta number: ")))
arv = (int(input("Mitu kujundit tahad (1-100): ")))

def viisnurk():
    pass

def ring():
    pass

def ruut(a):
    for j in range(a):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        turtle.lt(random.randint(0,90))
        for i in range(4):
            turtle.fd(100)
            turtle.lt(90)
    print("Valisid ruudu")
    pass

def suvaline():
    pass

if kujund == 1:
    viisnurk()
elif kujund == 2:
    ring()
elif kujund == 3:
    ruut(arv)
else:
    suvaline()

turtle.done