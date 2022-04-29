
# vytvořte třídu dum
# ma promennou pocet mistností
# má metodu uklid
# metoda uklid printuje bylo uklizeno pocet mistnosti
# vytvorte dva domy, panelak a rodinny
# panelaku dejte 500 mistnosti
# rodinnemu domu dejte 5 mistnosti
# uklidte panelak (co vám píše?)
# uklidte rodinny dum (co vám píše?)

from enum import Enum

class TypDomu(Enum):
    NEZADANO = ""
    PANELAK = "panelaku"
    RODINNY_DUM = "rodinnem dome"

class Dum():
    typ_domu = TypDomu.NEZADANO
    mistnosti = 0
    
    def uklid(self):
        print("v", self.typ_domu.value,"bylo uklizeno", self.mistnosti, "mistnosti")
        
rodinny_dum = Dum()
rodinny_dum.mistnosti = 5
rodinny_dum.typ_domu = TypDomu.RODINNY_DUM
panelak = Dum()
panelak.mistnosti = 500
panelak.typ_domu = TypDomu.PANELAK

print(TypDomu.PANELAK == panelak.typ_domu)

rodinny_dum.uklid()
panelak.uklid()
