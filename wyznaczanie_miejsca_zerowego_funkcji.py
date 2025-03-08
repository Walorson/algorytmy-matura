def f(x):
    return x**2 - 4

def bisekcja(f, a, b, dokladnosc = 0.01):
    while abs(a - b) > dokladnosc:
        c = (a + b) / 2
        print("f(c): ", f(c))

        if f(c) == 0:
            return c
        elif f(c) > 0:
            b = c
        else:
            a = c

        print(a, b)

    return c

print(bisekcja(f, -10, 10))