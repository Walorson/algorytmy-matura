def szybkie_potegowanie_modulo(a, n, modulo):
    wynik = 1

    while n > 0:
        if n % 2 == 1:
            wynik = (wynik * a) % modulo

        a = (a * a) % modulo
        n //= 2

    return wynik

print(2**100000011 % 17) #32 % 17 = 13
print(szybkie_potegowanie_modulo(2, 100000011, 17)) #32 % 17 = 13
#ten algorytm z takimi liczbami radzi se w milisekude (w przeciwieństwie do normalnego modulo tam!)