# Küsi kasutajalt inimeste arv ja ühe bussi kohtade arv
inimesed = int(input("Sisesta inimeste arv: "))
kohtade_arv = int(input("Sisesta ühe bussi kohtade arv: "))

# Arvuta busside arv ja viimases bussis olevate inimeste arv
busse = (inimesed - 1) // kohtade_arv + 1
viimases_bussis = inimesed - busse * kohtade_arv
viimases_bussis = inimesed % kohtade_arv

# Väljasta tulemus
print(f"Vaja on {busse} bussi. Viimases bussis on {viimases_bussis} inimest.")