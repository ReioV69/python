# 16.10.2024
# Ülesanded 4


#Kingituste pakkimine
try:
    kast = 5
    kingitusteArv = int(input("Lisa kingituste arv: "))
    komplektid = kingitusteArv // kast #täisarvu saamine
    yle = kingitusteArv % kast # jäägi jäämine
    print(f"Saad teha {komplektid} täis kinkekasti, üle jääb {yle} kingitust.")
except:
    print("saLisasid koguse valesti")

#Faili allalaadimine
try:

    failisuurus = int(input("Sisesta faili suurus: "))
    downlkiirus = int(input("Sisesta allalaadimise kiirus: "))
    aeg = failisuurus/downlkiirus
    print(f"Allalaadimiseks kulub {aeg} sekundit")
except:
    print("Palun siseta täisarvu!")

#Raamatute allahindulus
ale = 0.3
hind = 12.5
kogus = int(input("Lisa raamatute kogus: "))
summa = (hind-(hind*ale)) * kogus
print(f"{kogus} raamatu hind soodustusega on {summa:0.2f}€.")

#Aia pikkus
a = int(input("Lisa 1 külg: "))
b = int(input("Lisa 2 külg: "))
p = 2*(a+b)
print(f"Aia kogupikkus on {p} meetrit.")
