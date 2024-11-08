import random
#Ülesanne 10
#Reio Viikmaa
#08.11.24

#1
# arvud = []

# loop = 1

# while loop==1:
#     arv = (input("Sisesta arv: "))
#     if arv == "":
#         loop = 0
#         break 
#     arvud.append(int(arv))


# print(sum(arvud)/len(arvud))

# Arvu äraarvamise mäng
# Kirjutage Pythoni skript, mis simuleerib arvu äraarvamise mängu.
# Programm peab esmalt genereerima juhusliku arvu vahemikus 1 -10.
# Seejärel küsib programm kasutajalt arve, püüdes ära arvata genereeritud arvu. Kasutaja jätkab arvude sisestamist, kuni ta arvab õige arvu ära. Iga kord, kui kasutaja sisestab arvu, peab programm andma tagasisidet, kas pakutud arv on õige või mitte.
# Pärast õige arvu äraarvamist teavitab programm kasutajat, mitmenda katsega õige arv ära arvati, ja küsib, kas kasutaja soovib mängida uuesti.
# Kui kasutaja vastab jaatavalt, genereerib programm uue juhusliku arvu ja mäng algab otsast peale.
# Kui kasutaja otsustab mitte jätkata, tänab programm kasutajat mängus osalemise eest ja kuvab kõik senised tulemused: mitmenda katsega igal korral õige arv ära arvati.
# Programm peab kasutama while-tsüklit nii arvude sisestamise protsessi juhtimiseks kui ka mängu kordamise otsustamiseks
tulemused = []
katsed = 0
loop = 1

arv = random.randint(1,10)
print(arv)
while loop==1:
    katsed +=1
    vastus = int(input("Arva ära arv 1-10: "))
    if vastus == arv:
        print("Õige")
        print(f"Arvasid {katsed} korda")
        tulemused.append(katsed)
        uuesti = input("Kas soovid veel (j/e): ")
        if uuesti == "j":
            katsed = 0
            arv = random.randint(1,10)
            print(arv)
        else:
            break
    else:
        print("Proovi uuesti")

print("Mäng sai läbi")
print(tulemused)
