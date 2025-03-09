import string

def szyfr_playfair(tekst: str, klucz: str):
    alphabet = string.ascii_uppercase
    klucz = klucz.upper()
    tekst = tekst.upper()
    szyfr = ""

    if len(tekst) % 2 == 1:
        tekst += "X"

    macierz = [[None for x in range(5)] for x in range(5)]
    n = 0
    wypisywanie_szyfra = True

    for i in range(5):
        for j in range(5):
            if wypisywanie_szyfra == True:
                macierz[i][j] = klucz[n]

                n += 1
                if n >= len(klucz):
                    wypisywanie_szyfra = False
                    n = 0
            else:
                while klucz.__contains__(alphabet[n]) or alphabet[n] == "J": # i = j (w przypadku szyfru playfair)
                    n += 1

                macierz[i][j] = alphabet[n]
                n += 1

    for i in range(0, len(tekst), 2):
        a = kordy(tekst[i], macierz)
        b = kordy(tekst[i + 1], macierz)

        if a[1] == b[1]: # ta sama współrzędna Y
            a[0] = (a[0] + 1) % 5
            b[0] = (b[0] + 1) % 5  #prosty triczek z modulo, jeśli współrzędna jest = 5 (czyli wykracza po za granice tablicy) to modulo samo zamieni to na 0 :P

        elif a[0] == b[0]: # ta sama współrzędna X
            a[1] = (a[1] + 1) % 5
            b[1] = (b[1] + 1) % 5 

        else:
            a[0], b[0] = b[0], a[0]

        szyfr += macierz[a[1]][a[0]]
        szyfr += macierz[b[1]][b[0]]
   

    return szyfr

def kordy(element, tab):
    for i in range(0, len(tab)):
        for j in range(0, len(tab)):
            if tab[i][j] == element:
                return [j, i] #X, Y


print(szyfr_playfair("POLSKA", "ORZEL"))
print(szyfr_playfair("SIEMA", "BLORPY"))