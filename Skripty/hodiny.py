# třída hodiny
# má metody....
# kolik_je_hodin -> řekne nám počet hodin

import datetime

class Hodiny:
    casove_pasmo = 0
    
    def __init__(self, pasmo):
        self.casove_pasmo = pasmo
    
    def kolik_je_hodin(self):
        ted_je = datetime.datetime.now()
        print(ted_je.hour)
    
    def kolik_je_hodin_v_londyne(self):
        ted_je = datetime.datetime.now()
        print(ted_je.hour - self.casove_pasmo)
        
class Hodinky(Hodiny):
    pasek = "kozeny"
    pass
    
moje_hodinky = Hodinky(1)
#moje_hodiny.kolik_je_hodin()
moje_hodinky.kolik_je_hodin_v_londyne()
print(moje_hodinky.pasek)
