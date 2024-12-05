
fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))
print(vastuvõetud)
fail.close()


a = int(input("Palun sisestage, millise aasta andmeid vajate? "))

print(vastuvõetud[int(a[3])-1])


fail = open("konto.txt", encoding="UTF-8")

for rida in fail:
    if int(rida) > 0:
        print(rida, end="")