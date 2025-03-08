#Wyszukiwanie wzorca
def szukaj(wzorzec, tekst):
    poprawnosc = 0 #za każdą poprawną literę w ciągu jest przyznawany punkt do poprawności, jeśli poprawność będzie równa długościowi wzorca, znaczy to, że cały wzorzec został odnaleziony

    for i in range(0, len(tekst)):
        for j in range(0, len(wzorzec)):
            if i + j < len(tekst) and wzorzec[j] == tekst[i + j]:
                poprawnosc += 1

        if poprawnosc == len(wzorzec):
            return i #zwraca na jakim indexie zaczyna się wzorzec
        else:
            poprawnosc = 0
            
print(szukaj("DUPA", "MICHAL TO DUPA XD"))