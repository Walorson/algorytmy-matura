def sqrt(n, dokladnosc = 0.00001):
    if n < 0:
        return "LICZBA NIE JEST RZECZYWISTA"
    elif n == 0:
        return 0

    x1 = n / 2
    x2 = 0

    while True:
        x2 = (x1 + n / x1) / 2

        if abs(x1 - x2) < dokladnosc:
            break
        else:
            x1 = x2

    return x2

print(sqrt(7))