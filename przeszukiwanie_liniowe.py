def szukaj(n, tab):
    index = 0
    for i in tab:
        if i == n:
            return index
        
        index += 1

    return "NIE ZNALEZIONO"

tablica = [x for x in range(0, 101) if x % 2 == 0]
print("POZYCJA NA KTÓREJ ZNALEZIONO: ", szukaj(6, tablica))