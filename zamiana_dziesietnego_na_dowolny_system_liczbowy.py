#Szybkie odnajdywanie liczb pierwszych

def dziesietny_na(liczba, system):
    if system <= 1:
        return "SYSTEM JEDYNKOWY NIE ISTNIEJE"

    wynik = ""
    
    while liczba > 0:
        reszta = liczba % system
        if reszta == 10: 
            wynik += "A"
        elif reszta == 11:
            wynik += "B"
        elif reszta == 12:
            wynik += "C"
        elif reszta == 13:
            wynik += "D"
        elif reszta == 14:
            wynik += "E"
        elif reszta == 15:
            wynik += "F"
        else:
            wynik += str(reszta)

        liczba //= system

    return wynik[::-1]

print(dziesietny_na(32, 2))