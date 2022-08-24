fogadooralista = []

with open("TXT_allomanyok/fogado.txt", encoding="utf8") as f:
    for adat in f:
        sor = adat.strip().split(" ")
        tanar = sor[0]+" "+sor[1]
        foglaltido = sor[2]
        foglalasdatuma = sor[3]
        fogadooralista.append([tanar,foglaltido,foglalasdatuma])

for tanar,foglaltido,foglalasdatuma in fogadooralista:
    print(foglaltido)

