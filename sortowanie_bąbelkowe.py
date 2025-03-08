tab = [28,4,-1,123,0,5,82,63,13]

def sortowanie_babelkowe(tab):
    sortowanie_punkty = 0 #jeśli 2 liczby obok siebie są posortowane to tablica dostaje punkt za sorta

    while sortowanie_punkty < len(tab):
        for i in range(0, len(tab)):
            if i + 1 >= len(tab):
                break

            if tab[i] > tab[i + 1]:
                temp = tab[i]

                tab[i] = tab[i + 1]
                tab[i + 1] = temp
            else:
                sortowanie_punkty += 1

    return tab

print(sortowanie_babelkowe(tab))