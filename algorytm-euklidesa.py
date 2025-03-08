#Największy wspólny dzielnik
def NWD(a, b):
    while True:
        if b != 0:
            reszta = a % b
        else:
            break

        a = b
        b = reszta

    return a

def NWW(a, b):
    return int((a * b) / NWD(a, b))

print(NWD(48, 78))
print(NWW(48, 78))