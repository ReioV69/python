
# fail = open("rebased.txt", encoding="UTF-8")

# vastuvõetud = []

# for rida in fail:
#     vastuvõetud.append(int(rida))
# print(vastuvõetud)
# fail.close()


# a = int(input("Palun sisestage, millise aasta andmeid vajate? "))

# print(vastuvõetud[int(a[3])-1])


# fail = open("konto.txt", encoding="UTF-8")

# for rida in fail:
#     if int(rida) > 0:
#         print(rida, end="")


# valik = input("Sisesta faili nimi:")
# fail = open(valik)
# read = fail.readlines()
# mitmes = 1
# for i in read:
#     print(mitmes, i, end="")
#     mitmes +=1

# lugu = int(input(" Siseta loonumber: "))
# fail = open(valik)
# read = fail.readlines()

# print("mängi lugu",read[lugu-1])

from datetime import *

fail = open("nimekiri.txt")
read = fail.readlines()
print(read[datetime.now().day-1])
