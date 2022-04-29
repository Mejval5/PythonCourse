def fib(od, do):
    if do == 1:
        return [1]
    
    if do == 2:
        return [1, 1]
    
    sekvence = [1, 1]
    for i in range(2, do):
        nove_cislo = sekvence[i - 1] + sekvence[i - 2]
        sekvence.append(nove_cislo)
        
    return sekvence[od:]

vysledek_sekvence = fib(2, 20)
print(vysledek_sekvence)
