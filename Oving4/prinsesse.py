from sys import *
import traceback

def subgraftetthet(nabomatrise, startnode):
    n = len(nabomatrise)
    # SKRIV DIN KODE HER
    subgraf = [False] * n
    subgraf[startnode] = True
    queue = [startnode] # BFS
    while len(queue) > 0:
        fra = queue.pop(0)
        for til in range(0, n):
            if nabomatrise[fra][til] and not subgraf[til]:
                subgraf[til] = True
                queue.append(til)
    noder = 0
    kanter = 0
    for fra in range(0, n):
        if not subgraf[fra]:
            noder += 1
            for til in range(0, n):
                if nabomatrise[fra][til] and not subgraf[til]:
                    kanter += 1
    if noder == 0:
        return 0.0
    else:
        return float(kanter) / float(noder**2)


try:
    n = int(stdin.readline())
    nabomatrise = [None] * n # rader
    for i in range(0, n):
        nabomatrise[i] = [False] * n # kolonner
        linje = stdin.readline()
        for j in range(0, n):
            nabomatrise[i][j] = (linje[j] == '1')
    for linje in stdin:
        start = int(linje)
        print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
except:
    traceback.print_exc(file=stderr)