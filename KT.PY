#Reio Viikmaa 18.12.24
#KT

#5
 #Shopping List Create a program that will keep track of items for a shopping list. The program should keep asking for new items until nothing is entered (no input followed by enter/return key). The program should then display the full shopping list.
#Siia koguneb poe tooted mis lisad
poe_list = []
#Lõpmatu loop, et koguda tooted
while True:
    #Küsib tooteid
    toode = input("Lisa toode poe ostunimekirja (või vajuta Enter, et lõpetada:) ")

    #Vaatab kas input on tühi
    if toode == "":
        break #Lahkub loopist kui on tühi
      
    #Lisab toote poe listi
    poe_list.append(toode)

# Prindib välja kogu poe listi
print("\nSinu poe list")
for index, item in enumerate(poe_list, start=1):
    print(f"{index}. {item}")


#8 8. Täringud
"""
	kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
	kasutaja võistleb kahe täringuga arvuti vastu - 1p
	kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
	kood kommenteeritud - 1p
"""
import random
#funktisoon täringu keerutamiseks, see annab 2 juhuslikku arvu 1-6
def keeruta_taringut():
    return random.randint(1, 6), random.randint(1, 6)
#mängu põhifunktsioon
def mäng():
    print("Tere tulemast täringumängu!")
    raha = 100 #mängija raha alguses
    while raha > 0:
        panus = int(input(f"Teil on {raha} eurot. Kui palju soovite panustada? "))
        if panus > raha:
            print("Teil pole nii palju raha!")
            continue 
    #veeretab täringud kasutaja ja arvuti jaoks
        kasutaja_täringud = keeruta_taringut()
        arvuti_täringud = keeruta_taringut()
    #arvutab täringute summa
        kasutaja_summa = sum(kasutaja_täringud)
        arvuti_summa = sum(arvuti_täringud)
    #prindib täringud ja summa
        print(f"Teie täringud: {kasutaja_täringud} (summa: {kasutaja_summa})")
        print(f"Arvuti täringud: {arvuti_täringud} (summa: {arvuti_summa})")
    #kontrollib kes võitis ja uuendab raha summat
        if kasutaja_summa > arvuti_summa:
            raha += panus
            print(f"Te võitsite {panus} eurot!")
        elif kasutaja_summa < arvuti_summa:
            raha -= panus
            print(f"Te kaotasite {panus} eurot!")
        else:
            print("Viik! Raha jääb samaks.")
#kontrollib kas raha on otsas
        if raha == 0:
            print("Teil on raha otsas. Mäng läbi!")    
#käivitab mängu kui skript käivitatakse
mäng()



#7
# Eurokalkulaator
# Tere tulemast eurokalkulaatorisse!
print("Tere tulemast eurokalkulaatorisse!")

# Küsib kasutajalt, millises suunas ta soovib valuutat konverteerida
valik = input("Valige konverteerimise suund (EUR->EEK või EEK->EUR): ").strip().upper()

# Kontrollib, kas kasutaja valik on korrektne
if valik not in ["EUR->EEK", "EEK->EUR"]:
    # Kui valik on vale, kuvab veateate
    print("Vale valik! Palun valige kas 'EUR->EEK' või 'EEK->EUR'.")
else:
    # Kui valik on õige, küsib valuuta kogust
    kogus = float(input("Sisestage valuuta kogus: "))

    # Kontrollib, kas valik on EUR->EEK
    if valik == "EUR->EEK":
        # Arvutab EUR->EEK konverteerimise
        tulemus = kogus * 15.6466
        # Kuvab tulemuse
        print(f"{kogus} EUR on {tulemus:.2f} EEK.")
    # Kontrollib, kas valik on EEK->EUR
    elif valik == "EEK->EUR":
        # Arvutab EEK->EUR konverteerimise
        tulemus = kogus / 15.6466
        # Kuvab tulemuse
        print(f"{kogus} EEK on {tulemus:.2f} EUR.")
#10
"""Kaugushüpe
	kasutaja sisestab 3 kaugushüppe tulemust - 1p
	sinu programm leiab ning väljastab parima ja keskmise tulemuse - 2p
	programmi dialoog kasutajaga on arusaadav ja üheselt mõistetav - 1p
	kood kommenteeritud - 1p"""
#küsib 3 kaugushüppe tulemust
hypped = []
for i in range(3):
    tulemus = float(input(f"Sisesta {i+1}. kaugushüppe tulemus: ")) # i+1 et alustaks 1-st mitte 0-st
    hypped.append(tulemus)

#leiab parima ja keskmise tulemuse
parim_tulemus = max(hypped)
keskmine_tulemus = sum(hypped) / len(hypped)

#prindib tulemused
print(f"Parim tulemus: {parim_tulemus} meetrit")
print(f"Keskmine tulemus: {keskmine_tulemus} meetrit")
#16
