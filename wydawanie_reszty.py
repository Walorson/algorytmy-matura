def wydawanie_reszty(kwota):
    nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    reszta = []

    for nominal in nominaly:
        if nominal <= kwota:
            reszta.append(nominal)
            kwota -= nominal
        else:
            continue

    return reszta

print(wydawanie_reszty(200.01))