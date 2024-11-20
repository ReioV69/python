# Reio Viikmaa 20.11.24
import datetime
import os
# OS kasutajanimi
print(os.getlogin())
#os kataloog
print(os.getcwd())
try:
    mitu = 3
    x = datetime.datetime.now()
    for i in range(mitu):
        y = (x.strftime("%d%m%Y"))
        os.mkdir(str(y)+"_"+str(i+1))
except:
    print("Kataloogid juba olemas")
valik = input("Lisa kataloogi nimi kustutamiseks: ")
try:
    os.rmdir(valik)
except:
    print("Sellist kataloogi ei saa kustudada!")

items = os.listdir()
for item in items:
    if os.path.isdir(item):
        print(item)

