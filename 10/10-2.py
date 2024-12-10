import sys
input = sys.stdin

def makeInt(line):
    return list(map(int,line))

topo = list(map(makeInt,list(map(list,input.read().split('\n')))))

def getScore(topo, i, j, seen):
    if topo[i][j] == 9:
        if (i,j) not in seen:
            seen[(i,j)] = 0
        seen[(i,j)] += 1
        return
    val = topo[i][j]
    
    if i > 0 and topo[i-1][j] == val + 1:
        getScore(topo, i-1, j, seen)
    if i < len(topo)-1 and topo[i+1][j] == val + 1:
        getScore(topo, i+1, j, seen)
    if j > 0 and topo[i][j-1] == val + 1:
        getScore(topo, i, j-1, seen)
    if j < len(topo[0])-1 and topo[i][j+1] == val + 1:
        getScore(topo, i, j+1, seen)
    

total = 0
for i in range(len(topo)):
    for j in range(len(topo[0])):
        if topo[i][j] == 0:
            nines = {}
            getScore(topo, i, j, nines)
            for peak in nines.keys():
                total += nines[peak]

print(total)