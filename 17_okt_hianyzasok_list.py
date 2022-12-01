hianyzasoklista = []
with open("TXT_allomanyok/naplo.txt", encoding="utf8") as f:
    for adat in f:
        sor = adat.strip().split(" ")
        if sor[0] == "#":
            honap = int(sor[1])
            nap = int(sor[2])
        else:
            nev = sor[0]+" "+sor[1]
            hianyzas = sor[2]
            hianyzasoklista.append([honap,nap,nev,hianyzas])


print(f"2. feladat\nA naplóban {len(hianyzasoklista)} bejegyzés van.")

igazoltdb, igazolatlandb = 0,0
for honap,nap,nev,hianyzas in hianyzasoklista:
    for elem in hianyzas:
        if elem == "X":
            igazoltdb += 1
        if elem == "I":
            igazolatlandb +=1
print(f"3. feladat\nAz igazolt hiányzások száma {igazoltdb}, az igazolatlanoké {igazolatlandb} óra")