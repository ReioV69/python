import turtle
t = turtle.Turtle() #sünnitan uue kilpkonna nimega "T"
# Reio Viikmaa 08.10.2024
# Harjutus 3
"""
Ülesanne 3.3: Reisiplaan
Loo muutuja sihtkoht, mis sisaldab reisi sihtkohta (string)
Loo muutuja paevade_arv, mis näitab, mitu päeva reis kestab (integer)
Loo muutuja oobimise_hind, mis näitab ühe öö hinna (float)
Trüki välja lause, mis ühendab need andmed, nt: “Minu reis Soome kestab 5 päeva ja üks öö maksab 30.50 eurot.”
"""
# teksti liitmiseks kasutame ,
sihtkoht = "Tallinn"
paevade_arv = 2
oobimisehind = 15.5
print("Minu reis", sihtkoht, "kestab",paevade_arv,"päeva ja üks öö maksab" ,oobimisehind,"eurot.")





"""
Ülesanne 3.4: Lemmikraamat
Loo muutuja raamatu_pealkiri, mis sisaldab raamatu pealkirja (string)
Loo muutuja lehekylgede_arv, mis näitab raamatu lehekülgede arvu (integer)
Loo muutuja hindamisskoor, mis näitab raamatu hinnet skaalal 1-10 (float)
Trüki välja lause, nt: “Minu lemmikraamat on Sipsik, mis on 16 lehekülge pikk ja mille ma hindan 9.7 punktiga
"""
raamatupealkiri = "Sipsik"
lehekylgede_arv = 50
hindamisskoor = 10.4
print("Minu lemmikraamat on "+raamatupealkiri+", mis on "+str(lehekylgede_arv)+" lehekülge pikk ja mille ma hindan"+str(hindamisskoor)+"punktiga")
"""
Ülesanne 3.6: Python Turtle
Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
Loo muutuja kujundi_varv, mis määrab kujundi täitevärvi (string)
Kasutades Turtle’i, joonista kõrvuti värvilised kujundid ruut ja kolmnurk, mis kasutab loodud muutujaid
"""

k = 100
c = "red"
t.pencolor(c)
for i in range(4):
    t.fd(k)
    t.lt(90)
    
t.penup()
t.goto(k*1.5,0)
t.pendown()

for i in range(3):
    t.fd(k)
    t.lt(120)

turtle.done()