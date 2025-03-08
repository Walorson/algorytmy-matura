#Działa tylko na tablicy posortowanej
def szukaj(n, tab):
    lewy = 0
    prawy = len(tab) - 1

    while lewy != prawy:
        index_podzialu = int((lewy + prawy) / 2)

        if tab[index_podzialu] < n:
            lewy = index_podzialu + 1
        elif tab[index_podzialu] > n:
            prawy = index_podzialu
        else:
            return index_podzialu


    return "NIE ZNALEZIONO"

tablica = [3, 5, 9, 16, 21, 33, 39, 40, 42, 49, 55, 61, 69, 73, 81, 89, 92, 95, 99]
print("POZYCJA NA KTÓREJ ZNALEZIONO: ", szukaj(33, tablica))