wspolczynniki = [3, 2, 4, -1] #3x^3 + 2x^2 + 4x - 1

def schemat_hornera(x, w):
    wynik = w[0]

    for i in range(1, len(w)):
        wynik = x * wynik + w[i]

    return wynik

print(schemat_hornera(2, wspolczynniki))