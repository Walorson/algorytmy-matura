import string

def szyfr_cezara(tekst, klucz):
    szyfr = ""
    tekst = tekst.upper()
    alfabet = string.ascii_uppercase
    for litera in tekst:
        gdzie = alfabet.find(litera)

        gdzie += klucz
        if gdzie >= len(alfabet):
            gdzie = gdzie - len(alfabet)

        szyfr += alfabet[gdzie]

    return szyfr

print(szyfr_cezara("DUPA", 14))