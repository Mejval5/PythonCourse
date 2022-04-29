def zmen(data):
    data[1] = 50

def vynasob_kazde_cislo_dvema(data):
    delka_seznamu = len(data)
    for index in range(delka_seznamu):
        cislo = data[index]
        cislo = cislo * 2
        data[index] = cislo

data = [5, 10, 20]

print("data pred zmenou:", data)

zmen(data)

print("data po zmene:", data)