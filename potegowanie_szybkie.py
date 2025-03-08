def szybkie_potegowanie(a, n):
    wynik = 1

    while n > 0:
        if n % 2 == 1:
            wynik *= a

        a *= a
        n //= 2

    return wynik

print(szybkie_potegowanie(2, 6))