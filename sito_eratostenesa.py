#Szybkie odnajdywanie liczb pierwszych

tab = [x for x in range(2, 101)]

def sito_eratostenesa(tablica):
    dlugosc_tablicy = len(tablica)
    
    for i in range(2, int(dlugosc_tablicy ** 1/2)):
       
        j = i + i
        while j <= dlugosc_tablicy + 1:
            try:
                tablica.remove(j)
            except ValueError:
                pass

            j += i

    return tablica

print(sito_eratostenesa(tab))