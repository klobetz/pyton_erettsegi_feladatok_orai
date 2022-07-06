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



