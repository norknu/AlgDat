from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    # SKRIV DIN KODE HER
    start = Node()
    for (ord, posisjon) in ordliste:
        node = start
        for bokstav in ord:
            if not bokstav in node.barn:
                node.barn[bokstav] = Node()
            node = node.barn[bokstav]
        node.posi.append(posisjon)
    return start

def posisjoner(ord, indeks, node):
    # SKRIV DIN KODE HER
    if indeks >= len(ord):
        posi = node.posi
    elif ord[indeks] == "?":
        posi = []
        for barn in node.barn.values():
            posi += posisjoner(ord, indeks + 1, barn)
    elif ord[indeks] in node.barn:
        posi = posisjoner(ord, indeks + 1, node.barn[ord[indeks]])
    else:
        posi = []
    return posi


try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o,pos) )
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
except:
    traceback.print_exc(file=stderr)