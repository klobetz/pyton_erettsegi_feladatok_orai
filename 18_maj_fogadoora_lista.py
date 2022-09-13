from datetime import datetime

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

#4. feldat:
#valaszido = input("4. feladat\nAdjon meg egy érvényes időpontot (pl. 17:10): ")
valaszido ="17:40"
tanaroklista = []
for tanar,foglaltido,foglalasdatuma in fogadooralista:
    if foglaltido == valaszido:
        tanaroklista.append(tanar)

tanaroklista = sorted(tanaroklista)
#tanaroklista.sort(reverse=True) #fordított sorrend
#tanaroklista.sort()
#fajlnev = valaszido[:2]+valaszido[3:]+".txt"

for elem in tanaroklista:
    print(elem)
with open(f"Kiiratasok/{valaszido.replace(':','')}.txt", "w" , encoding="utf8") as f:
    for elem in tanaroklista:
        f.write(f"{elem}\n")

#5. feladat:
legkisebbdatum = datetime.max
#print(legkisebbdatum)
for tanar,foglaltido,foglalasdatuma in fogadooralista:
    idopont = datetime.strptime(foglalasdatuma, "%Y.%m.%d-%H:%M")
    #print(idopont)
    if idopont < legkisebbdatum:
        legkisebbdatum = idopont
        adaotttanar = tanar
        adottidopont = foglaltido


#print(legkisebbdatum)
print(f"\n5. feladat:\nTanár neve: {adaotttanar}\nFoglalt időpont: {adottidopont}\nFoglalás ideje: {legkisebbdatum:%Y.%m.%d-%H:%M}")
