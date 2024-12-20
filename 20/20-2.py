import sys
input = sys.stdin
grid = list(map(list,input.read().split('\n')))
mods = [[-1,0],[1,0],[0,-1],[0,1]]
start = None
# First, find the default path
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i,j)
            break
    if start != None:
        break

def getJumps(path, startPoint):
    out = {}
    seen = set()
    toSee = [startPoint]
    getJumpsRec(path, toSee, 0, seen, out)
    return out

def getJumpsRec(path, toSee, depth, seen, out):
    newSee = []
    if depth > 20:
        return
    for p in toSee:
        if p in seen:
            continue
        seen.add(p)
        if p in path:
            out[p] = depth
        for m in mods:
            newSee.append((p[0] + m[0], p[1] + m[1]))
    getJumpsRec(path, newSee, depth + 1, seen, out)

runner = start
count = 0
mainPath = {}
checkPath = []
while grid[runner[0]][runner[1]] != 'E':
    checkPath.append(runner)
    mainPath[runner] = count
    count += 1
    for mod in mods:
        new = (runner[0] + mod[0], runner[1] + mod[1])
        if new not in mainPath and (grid[new[0]][new[1]] == '.' or grid[new[0]][new[1]] == 'E'):
            runner = new
            break
mainPath[runner] = count
checkPath.append(runner)

shorted = 0
for jumpStart in mainPath.keys():
    jd = getJumps(mainPath, jumpStart)
    for j in jd:
        if j in mainPath:
            shaved = mainPath[j] - mainPath[jumpStart] - jd[j]
            if shaved >= 100:
                shorted += 1

print(shorted)