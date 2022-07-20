autoklista = []
with open("TXT_allomanyok/autok.txt", encoding="utf8") as f:
    for adat in f:
        sor = adat.strip().split()

        nap = int(sor[0])
        ido = sor[1]
        rendszam = sor[2]
        azonosito = int(sor[3])
        km = int(sor[4])
        kibehajtas = int(sor[5])
        adatok = [nap,ido,rendszam,azonosito,km,kibehajtas]
        autoklista.append(adatok)

#2. Adja meg, hogy melyik autót vitték el utoljára a parkolóból! Az eredményt a mintának megfelelően írja a képernyőre!

for elem in autoklista:
    if elem[5] == 0:
        nap1 = elem[0]
        rendszam1 = elem[2]

print(f"2. feladat\n{nap1} nap rendszám: {rendszam1} ")

#3. Kérjen be egy napot és írja ki a képernyőre a minta szerint, hogy mely autókat
# vitték ki és hozták vissza az adott napon!

print("3. feladat")
#bekertnap = int(input("Nap: "))
bekertnap = 4
for elem in autoklista:
    # if elem[5] == 0:      #ez felesleges f.stringgel megoldható
    #     ki = "ki"
    # else:
    #     be = "be"

    if elem[0] == bekertnap:
        if elem[5] == 0:
            print(f"{elem[1]} {elem[2]} {elem[3]} ki")
        else:
            print(f"{elem[1]} {elem[2]} {elem[3]} be")

#4. Adja meg, hogy hány autó nem volt bent a hónap végén a parkolóban!
print("4.feladat")
kihajtas = 0
behajtas = 0
for elem in autoklista:
    if elem[5] == 0:
        kihajtas += 1
    else:
        behajtas +=1
visszanemhozottautok = kihajtas-behajtas
print(f"A hónap végén {visszanemhozottautok} autót nem hoztak vissza.")

print("5.feladat:")
renedszamoklista = []
for elem in autoklista:
    if elem[2] not in renedszamoklista:
        renedszamoklista.append(elem[2])
renedszamoklista = sorted(renedszamoklista)
#print(renedszamoklista)

for adatrendszam in renedszamoklista:
    megtettkmek =[]
    for elem in autoklista:
        if adatrendszam == elem[2]:
            megtettkmek.append(elem[4])
    #print(adatrendszam,megtettkmek)
    kezdokm = megtettkmek[0]
    utolsokm = megtettkmek[-1]
    megtettkm = utolsokm-kezdokm
    print(f"{adatrendszam} {megtettkm} km")

