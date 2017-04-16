from sys import stdin

class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt 
        self.neste = None 

def spor(kubbe):
    # SKRIV DIN KODE HER
    liste = kubbe.vekt
    while kubbe.neste is not None:
        if kubbe.vekt>liste:
            liste = kubbe.vekt
        else:
            liste = liste
        kubbe = kubbe.neste
    return liste
# Oppretter lenket liste
forste = None
siste = None
for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste

print spor(forste)