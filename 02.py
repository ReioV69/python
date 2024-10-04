from math import *
# Reio Viikmaa
# Harjutus 02
# 30.09.24


# kolmnurga ümbermõõt
a = int(input("Lisa arv: "))
b = int(input("Lisa arv: "))
c = int(input("Lisa arv: "))
p = a + b + c
print("kolmnurga ümbermõõt on", p,"ühikut")

#toote hind
tootehind = 36.75
ale = 0.4
soodushind = tootehind - (tootehind * ale)
kogus = 3
kokku = soodushind * kogus

print(kokku,"€")



# 6. Rulluisutajad
kiirus = 29.9
aeg = 24/60
dist = kiirus * aeg
print("Rulluisutaja jõuab" , dist, "km kaugusele")


#pitsa
hind = 14.19
hind1 = hind / 3
print("Igaüks maksab" , hind1, "€")



#Hüpotenuus
a,b = 16,9
c = sqrt(a**2 + b**2)
print("Hüpotenuus on:", c)







#Ajateisendus
aeg =int(input("Lisa aeg minutites: "))
h = aeg/60
m = aeg % 60

print(h,":",m)

#Arvusüsteemid
arv = int(input("Lisa 10nd arv: "))
kahend = bin(arv)
kuust = hex(arv)
print("Sinu teisendused on: ", kahend, "ja", kuust)

#Kütusekulu arvutamine
l = int(input("Lisa tangitud liitrid:"))
km = int(input("Lisa läbitud kilomeetrid:"))
kytusekulu = l/(km/100)
print("Sinu kütusekulu on ", kytusekulu)