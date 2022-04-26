#accents = str.maketrans({'Á':'A',
#                         'Ž':'Z'})

def nasciSlovnik(path: str, encoding='ISO 8859-2') -> list[str]:
    """Funkce pro načtení slovníku z souboru formátu '*.dic'.

    Args:
        path (str): cesta k souboru
        encoding (str, optional): Kodování. Defaults to 'ISO 8859-2'.

    Returns:
        list[str]: senzma slov
    """
    from unidecode import unidecode

    slovnik = []
    with open(path, mode='r', encoding=encoding) as dic:
        for line in dic:
            line = line.strip()
            if line[-2:] == '/H' and len(line) > 6:
                #word = line[:-2].upper().translate(accents)
                word = unidecode(line[:-2].upper())
                slovnik.append(word)
    return slovnik

ascii_art = [
    """
     
          
           
            
            
      
     
    _____
    """,
    """
      _______
     |/      
     |      
     |       
     |       
     | 
     |
    _|___
    """,
    """
      _______
     |/      |
     |      
     |       
     |       
     | 
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |       
     |       
     | 
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |       |
     |       
     | 
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      \|
     |       
     | 
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     | 
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     | 
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
    """,
]
                
slovnik = nasciSlovnik('static/cs_CZ.dic')
print(f'Načteno {len(slovnik)} slov.') 

from random import choice
from re import X
hledane_slovo = choice(slovnik)
hracovo_slovo = '_' * len(hledane_slovo)
hracovy_zivoty = len(ascii_art)

while True:
    print('Slovo:', ' '.join(hracovo_slovo))
    hadani = input("Hadej: ").upper().strip()

    if hadani in hledane_slovo:
        for i, pismeno in enumerate(hledane_slovo):
            if hadani == pismeno:
                hracovo_slovo = hracovo_slovo[:i] + pismeno + hracovo_slovo[i+1:] 
    else:
        hracovy_zivoty -= 1
        if hracovy_zivoty == 0:
            print(f'Prohra, neuhlad jsi: {hledane_slovo}')
            exit(1)
        print(ascii_art[-hracovy_zivoty])
        
    if hracovo_slovo == hledane_slovo or hadani == hledane_slovo:
        print(f'Víteztví, uhádl jsi: {hledane_slovo}')
        exit(0)
a