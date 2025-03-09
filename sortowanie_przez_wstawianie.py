tab = [3, 1, 2, 5, 0]

def sortowanie_przez_wstawianie(tab):
    for i in range(1, len(tab)):
        klucz = tab[i]
        j = i - 1

        while j >= 0 and klucz < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1

        tab[j + 1] = klucz

    return tab


print(sortowanie_przez_wstawianie(tab))