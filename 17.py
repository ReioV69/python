# Reio Viikmaa 28.11.24
# Ülesanne 17


# meeste keskmised töötunnid, töötasu ning palk
# naiste keskmised töötunnid, töötasu ning palk
# Tulemused prindi konsooli

fail =  open("palgad.txt")
read = fail.readlines()
npalgad = []
mpalgad = []

for i in read:
    r = i.split(",")
    for j in range(1,7):
        print(r[j])
    if r[3] == "Mees": 
        mpalgad.append(float(r[6]))
    else:
        npalgad.append(float(r[6]))
print(mpalgad)
print(npalgad)


print(sum(mpalgad)/len(mpalgad))
print(sum(npalgad)/len(npalgad))



    








#Paratehingud
# kogu tehingute arvu
# positiivsete tehingute arvu
# positiivsete tehingute kogusumma




# fail = open("pangakonto.txt")
# tekstiread = (fail.readlines())
# tehingute_arv = len(tekstiread)
# pos_tehinguid = 0
# pos_tehingute_summa = 0

# for i in tekstiread:
#     if float(i.strip()) > 0:
#         pos_tehinguid += 1
#         pos_tehingute_summa +=float(i)

# print(f"Tehinguid kokku: {tehingute_arv}")
# print(f"Pos tehinguid kokku: {pos_tehinguid}")
# print(f"Tehingute summa: {pos_tehingute_summa}")


