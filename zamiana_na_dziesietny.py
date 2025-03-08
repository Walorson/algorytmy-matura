#Zamiana z dziesiętnego systemu liczbowy na dowolny inny

def na_dziesietny(liczba, system):
    liczba = str(liczba)[::-1]
    wynik = 0
    i = 0

    for cyfra in liczba:
        wynik += int(cyfra) * (system ** i)
        i += 1

    return wynik

print(na_dziesietny(11000011, 2))