#4.2
# def mahlapakkide_arv(ountekogus):
#     mahlapakkidearv = int(round(ountekogus * 0.4/3,0))
#     return mahlapakkidearv
# kg = int(input("Õunte kogus: "))
# print(mahlapakkide_arv(kg))


#4.1
# mitu = int(input("Mitu korda: "))
# lause = input("Sinu reklaamlause: ")

# for i in range(mitu):
#     print(lause.upper)

# def banner(l):
#     print(l.upper())

# for i in range(mitu):
#     banner(lause)

#4.3

# def eelarve(kylalistearv):
#     eelarve = kylalistearv * 10 + 55
#     return eelarve

# max_inimesed  = int(input("Mitu inimest on kutsutud: ?"))

# min_inimesed = int(input("Mitu inimest tuleb: ?"))
# print(f"Maksimaalne eelarve: {eelarve(max_inimesed)}")
# print(f"Minimaalne eelarve: {eelarve(min_inimesed)}")




#4.4

# def tervitus(tere):
#     for i in range(tere):
#         print("Võõrustaja: " "Tere!")
#         print(f"Täna {i+1}, kord tervitada, mõtiskleb võõrustaja.")
#         print("Külaline: " "Tere, suur tänu kutse eest!")
        

# tervitus(5)


#4.5
valik = int(input("Sisesta faili nimi: "))
def pronksikarva_summa(pronks):
    fail = open("mündid.txt", encoding="UTF-8")
    fail.readlines()

