from sys import stdin

# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner
True = 1
False = 0

class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0

def dfs(rot):
    # SKRIV DIN KODE HER
    ToDo = [rot]
    while ToDo:
        noden = ToDo[len(ToDo) - 1]
        if noden.ratatosk:
            return len(ToDo) - 1
        if noden.nesteBarn == len(noden.barn):
            ToDo.pop()
        else:
            ToDo.append(noden.barn[noden.nesteBarn])
            noden.nesteBarn += 1

def bfs(rot):
    # SKRIV DIN KODE HER
    todo = ([rot, 0])
    while len(todo) > 0:
        node = todo.pop(0)
        dyb = todo.pop(0)
        if node.ratatosk:
            return dyb
        for b in node.barn:
            todo.append((b, dyb + 1))



funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print bfs(start_node)
    # SKRIV DIN KODE HER
