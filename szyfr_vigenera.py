import string

def szyfr_vigenera(tekst: str, klucz: str):
    tekst = tekst.upper()
    alfabet = string.ascii_uppercase
    szyfr = ""
    j = 0

    for i in range(0, len(tekst)):
        litera1 = alfabet.find(tekst[i])
        litera2 = alfabet.find(klucz[j])

        j += 1
        if j >= len(klucz):
            j = 0

        nowa_litera = (litera1 + litera2) % len(alfabet)
        szyfr += alfabet[nowa_litera]
            

    return szyfr

print(szyfr_vigenera("BANANYJEM", "MALPA"))