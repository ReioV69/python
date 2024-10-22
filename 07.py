#22.10.24 Reio Viikmaa
# Ülesanne 7 Massiivid


# Aastaajad
kuud = [('jaanuar',3,2,-13,7,-16,8,6,-17,-4,0,-9,-7,-17,-19,-5,-3,8,-13,9,-19,0,-14,-19,6,-6,-5,-2,3,8,-7,-15),
('veebruar',-2,-1,-3,8,-19,3,8,-15,0,3,-20,-9,-6,-7,10,-1,-11,-15,-17,-2,3,-18,2,-3,-19,5,-6,-11),
('märts',10,9,5,3,-6,-11,-4,0,0,0,-19,-4,-15,-7,7,10,5,-17,-16,-19,-3,8,-10,-13,-19,-3,-6,-10,4,-20,10),
('aprill',1,4,3,0,-5,10,-15,-10,-19,-12,-6,-8,-15,-3,4,-5,1,-11,-16,-7,5,5,3,-8,-10,6,-6,-16,5,1,),
('mai',-4,-8,3,-20,-15,-3,4,6,-8,-4,-9,-9,9,-3,-17,4,-20,-7,-8,-8,-11,-17,-17,-8,-15,4,-13,-13,9,-16,-15),
('juuni',-10,-17,-11,-18,-19,-20,-3,-13,-17,-15,-5,-12,-6,-9,4,-8,-9,-2,1,-3,4,5,-15,-4,8,-18,3,-19,-6,-19,-4),
('juuli',-13,7,-20,-9,-11,8,-7,-10,1,-16,-10,-17,-9,2,4,-12,-12,-19,-8,-5,-9,0,9,7,-2,-11,-6,8,-13,8,),
('august',-20,3,-15,10,-15,-5,-13,-10,2,-7,-8,-15,-5,3,-7,-6,-11,-4,2,5,5,-19,-13,2,-8,7,-20,2,-12,-10,-14),
('september',-6,-6,-11,8,8,-12,9,10,-13,-14,2,-10,-8,7,-10,4,-4,-6,-3,-15,3,-4,-10,-18,-5,-5,3,-17,-20,-19),
('oktoober',-15,-20,-18,-16,6,3,9,-2,1,-8,-5,10,-8,-2,9,8,-16,-3,6,-8,8,-10,-18,7,7,7,10,-1,-13,-15,-9),
('november',-6,-14,-18,-15,-11,-14,6,0,-11,-7,-4,-10,-11,-4,3,8,-20,-12,7,-3,10,-12,-11,8,-20,3,-2,10,-6,-12,1),
('detsember',1,5,-8,-2,-19,-13,7,4,-10,-4,5,3,6,-10,-11,4,-20,4,-3,1,1,-7,3,-13,-12,-2,6,-2,6,-9,-13)]


print(f"Hetkekuu {kuud[9][0]}")
kuus_kokku = len(kuud[9])-1
print(f"Viimane mõõtmine: {kuud[9][kuus_kokku]}")
print("Selle kuu temperatuurid:")
ajutine = []
for i in range(kuus_kokku):
    ajutine.append(kuud[9][i+1])
    print(kuud[9][i+1], end=", ")
print(f"Max temp: {max(ajutine)}")
print(f"Min temp: {min(ajutine)}")
print(f"Keskmine temp: {round(sum(ajutine)/len(ajutine),2)}")
print(f"-20 esineb {ajutine.count(-20)} korda")
ajutine.pop(5-1)
#del ajutine[4]
ajutine.insert(5-1,16)
ajutine.sort()
print(ajutine)




"""
#Muusikapalad
laulud =['ALIKA – "Bridges"','Anett x Fredi – "Read Between The Lines"','villemdrillem – "leekiv armastus"','Clicherik & Mäx – "PAKSUD"','nublu – "ära ärata"','NOËP – "Move Your Feet"','Trad.Attack! – "Bring It On"','Bedwetters – "It Is What It Is"','Reket – "Panama paberid"','Grete Paia – "Võluväel"'
]

# Vali lugu
for i in range(10):
    print(str(i+1)+", "+laulud[i])
try:
    valik = int(input("Vali lugu 1-10:"))
    print(f"Mängin: {laulud[valik-1]}")
except:
    print("Tegid vale otsuse :)")
            
"""

