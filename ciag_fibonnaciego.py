#Wyznacz n-ty wyraz ciągu Fibonacci'ego

def fibonacci(n):
    a = 0
    b = 1
    wynik = None

    for i in range(0, n):
        wynik = a + b
        a = b
        b = wynik

    return a

print(fibonacci(7))