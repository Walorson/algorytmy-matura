def szyfrowanie_plotkowe(tekst, klucz):
    plotek = [[] for _ in range(klucz)]
    i = 0
    j = 0
    kierunek = "dół" #kierunek szyforwania liter w macierzy. Stawiane litery w tablicy tworzą wizualnie falę

    while i < len(tekst):
        plotek[j].append(tekst[i])
        i += 1
        
        if kierunek == "dół":
            j += 1
            if j == len(plotek) - 1:
                kierunek = "góra"

        elif kierunek == "góra":
            j -= 1
            if j == 0:
                kierunek = "dół"

    #spisanie tablicy na tekst
    szyfr = ""

    for i in plotek:
        for j in i:
            szyfr += j

    return szyfr

print(szyfrowanie_plotkowe("ZAKŁAMANY", 3))