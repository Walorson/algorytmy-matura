#Czy liczba jest pierwsza?
def czy_pierwsza(a):
    pierwsza = True

    if pierwsza == 1 or pierwsza == 0:
        return False

    for dzielnik in range(2, int(a / 2)):
        if a % dzielnik == 0:
            pierwsza = False
            break

    return pierwsza

print(czy_pierwsza(7))