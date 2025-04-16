def iteracije(N):
    broj = 5
    for i in range(N):
        broj= broj + 1/3
    for i in range(N):
        broj = broj + 1/3
    print(broj)

iteracije(200)
iteracije(2000)
iteracije(20000)

#broj 1/3 se ne može konaćno zapisati u konaćnom zapisu, stoga postoji mala greška u rezultatu
