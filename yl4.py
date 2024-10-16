# 16.10.2024
# Ülesanded 4

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
