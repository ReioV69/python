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

def keeruta_taringut():
    return random.randint(1, 6), random.randint(1, 6)

def mäng():
    print("Tere tulemast täringumängu!")
    raha = 100
    while raha > 0:
        panus = int(input(f"Teil on {raha} eurot. Kui palju soovite panustada? "))
        if panus > raha:
            print("Teil pole nii palju raha!")
            continue    
    
        kasutaja_täringud = keeruta_taringut()
        arvuti_täringud = keeruta_taringut()

        kasutaja_summa = sum(kasutaja_täringud)
        arvuti_summa = sum(arvuti_täringud)

        print(f"Teie täringud: {kasutaja_täringud} (summa: {kasutaja_summa})")
        print(f"Arvuti täringud: {arvuti_täringud} (summa: {arvuti_summa})")

        if kasutaja_summa > arvuti_summa:
            raha += panus
            print(f"Te võitsite {panus} eurot!")
        elif kasutaja_summa < arvuti_summa:
            raha -= panus
            print(f"Te kaotasite {panus} eurot!")
        else:
            print("Viik! Raha jääb samaks.")

        if raha == 0:
            print("Teil on raha otsas. Mäng läbi!")    
   
if __name__ == "__main__":
    mäng()



#7

#10

#16
