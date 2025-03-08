def potega(n, wykladnik):
    wynik = 1

    for i in range(0, wykladnik):
        wynik *= n

    return wynik

print(potega(2, 6))