# äratus_arv = int(input("Mitu korda äratus heliseb?: "))

# for i in range(äratus_arv):
#     print("Tõuse ja sära!")

# #2.2
# Ringid = int(input("Sisesta ringide arv: "))

# porgandid = 0

# ringide_arv = 1

# while ringide_arv <= Ringid:
#     if ringide_arv % 2 == 0:
#         porgandid += ringide_arv
#     ringide_arv += 1
    

# print(f"Porgandite koguarv on {porgandid}")


import random
# #2.3

# taringute_arv = int(input(f"Sisesta täringute arv: "))

# for i in range(taringute_arv):
#     veereta = random.randint(1, 6)
#     print(veereta)


#2.4
nisutera = 0
arv = int(input(f"Sisesta üks täisarv: "))
if arv > 64:
    print("Nii palju ruute pole")

korda = arv
if korda >= 1:
    nisutera += 1
    korda -= 1


while korda >= 1:
    korda -= 1
    nisutera *= 2
print(f"Leiduri palutud nisuterde arv {arv}. ruudu eest: {nisutera}")

ounade_arv = 14
ppoisse = 3
for i in range(ppoisse):
    ounade_arv -= (random.randint(1, 2))

print(f"Lumivalgekesele jääb alles {ounade_arv} õunu")