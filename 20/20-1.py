import sys
input = sys.stdin
grid = list(map(list,input.read().split('\n')))
mods = [[-1,0],[1,0],[0,-1],[0,1]]
jumps = [(-2,0),(-1,-1),(0,-2),(1,-1),(2,0),(1,1),(0,2),(-1,1)]
betweeners = {
    (-2,0): [(-1,0)],
    (-1,-1): [(-1,0), (0,-1)],
    (0,-2): [(0,-1)],
    (1,-1): [(1,0), (0,-1)],
    (2,0): [(1,0)],
    (1,1): [(1,0), (0,1)],
    (0,2): [(0,1)],
    (-1,1): [(-1,0), (0,1)]
}
start = None
# First, find the default path
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i,j)
            break
    if start != None:
        break

def isShortcut(path, startPoint, jumpDir):
    for midPoint in betweeners[jumpDir]:
        if (startPoint[0] + midPoint[0], startPoint[1] + midPoint[1]) in path:
            return False
    return True

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
    for j in jumps:
        jumpEnd = (jumpStart[0] + j[0], jumpStart[1] + j[1])
        if jumpEnd in mainPath and isShortcut(mainPath, jumpStart, j):
            shaved = mainPath[jumpEnd] - mainPath[jumpStart] - 2
            if shaved >= 100:
                shorted += 1

print(shorted)