import math

nekonecno = math.inf
not_a_number = math.nan

def deleni(x, y):
    if y == 0:        
        if x < 0:
            return -nekonecno
        elif x > 0:
            return nekonecno
        elif x == 0:
            return not_a_number    
    return x / y

print("5 / 0 :", deleni(5, 0))
print("-5 / 0 :", deleni(-5, 0))
print("0 / 0 :", deleni(0, 0))
print("5 / 1 :", deleni(5, 1))
print("5 / 18 :", deleni(5, 18))
print("5 / nekonecno :", deleni(5, nekonecno))