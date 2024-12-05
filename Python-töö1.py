print("Tere, maailm!")

aasta = 2020 
liblikas = "teelehe-mosaiikliblikas "
lause_keskosa = "aasta liblikas on "
lause = str(aasta) + " " + lause_keskosa +" " + liblikas
print(lause)
"""
#1.3
pilv = float(input(f"Pilvede aluse kõrgus (km): "))
if pilv > 6.0:
    print("Need on ülemised pilved")
else:
    print("Need ei ole ülemised pilved")
"""
#1.4


reisijate_arv = int(input("Reisijate arv: "))
kohtade_arv = int(input("Ühe bussi kohtade arv: "))

busse = (reisijate_arv - 1) // kohtade_arv + 1

if reisijate_arv % kohtade_arv == 0:   
    viimases_bussis = kohtade_arv
else:
  viimases_bussis = reisijate_arv % kohtade_arv



print(f"Vaja on {busse} bussi . Viimases bussis on {viimases_bussis} inimest.")



