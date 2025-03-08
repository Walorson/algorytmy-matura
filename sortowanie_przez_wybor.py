tab = [3, 1, 5, 2, 0]

def sortowanie_przez_wybor(tab):
    lewo = 0 #lewa granica tablicy
    for k in range(0, len(tab) - 1):
        najmniejsza = tab[lewo]
        najmniejsza_id = lewo

        for i in range(lewo + 1, len(tab)):
            if tab[i] < najmniejsza:
                najmniejsza = tab[i]
                najmniejsza_id = i

        tab[lewo], tab[najmniejsza_id] = tab[najmniejsza_id], tab[lewo] #zamiana miejscami
        lewo += 1

    return tab

print(sortowanie_przez_wybor(tab))