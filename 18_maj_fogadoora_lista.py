fogadooralista = []

with open("TXT_allomanyok/fogado.txt", encoding="utf8") as f:
    for adat in f:
        sor = adat.strip().split(" ")
        tanar = sor[0]+" "+sor[1]
        foglaltido = sor[2]
        foglalasdatuma = sor[3]
        fogadooralista.append([tanar,foglaltido,foglalasdatuma])

# for tanar,foglaltido,foglalasdatuma in fogadooralista:
#     print(foglaltido)

#2. feladat:
print(f"2. feladat\nFoglalások száma: {len(fogadooralista)}")

#3. feladat:
#valasztanar = input("3. feladat\nAdjon meg egy nevet: ")
valasztanar = "Nagy Ferenc"
#valasztanar = "Farkas Attila"
db = 0
for tanar,foglaltido,foglalasdatuma in fogadooralista:
    if tanar == valasztanar:
        db += 1

if db > 0 :
    print(f"{valasztanar} néven {db} időpontfoglalás van.")
else:
    print("A megadott néven nincs időpontfoglalás.")



