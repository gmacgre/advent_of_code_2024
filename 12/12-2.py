import sys
input = sys.stdin

grid = list(map(list,input.read().split('\n')))
directions = [[-1,0],[0,-1],[1,0],[0,1]]
seen = set()
totalPrice = 0

def inScope(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return False
    return True

def getNeighbors(grid, i, j):
    target = grid[i][j]
    toRet = []
    for dir in directions:
        if inScope(grid, i+dir[0], j+dir[1]) and grid[i+dir[0]][j+dir[1]] == target:
            toRet.append(True)
        else:
            toRet.append(False)
    return toRet

def matchDiag(grid, i, j, i_s, j_s):
    return inScope(grid, i+i_s, j+j_s) and grid[i+i_s][j+j_s] == grid[i][j]

def getAttributes(grid, i, j, target):
    if (i,j) in seen:
        return 0, 0
    seen.add((i,j))
    area = 1
    perim = 0
    #If there is a corner on this spot, increment perimeter. Otherwise, leave as 0
    hasUp, hasLeft, hasDown, hasRight = getNeighbors(grid, i, j)
    if not hasUp and not hasLeft:
        perim += 1
    if not hasLeft and not hasDown:
        perim += 1
    if not hasDown and not hasRight:
        perim += 1
    if not hasRight and not hasUp:
        perim += 1
    if hasUp and hasRight and not matchDiag(grid, i, j, -1,1):
        perim += 1
    if hasUp and hasLeft and not matchDiag(grid, i, j, -1,-1):
        perim += 1
    if hasDown and hasRight and not matchDiag(grid, i, j, 1,1):
        perim += 1
    if hasDown and hasLeft and not matchDiag(grid, i, j, 1,-1):
        perim += 1
    for dir in directions:
        if inScope(grid, i+dir[0], j+dir[1]) and grid[i+dir[0]][j+dir[1]] == target:
            newArea, newPerim = getAttributes(grid, i+dir[0], j+dir[1], target)
            area += newArea
            perim += newPerim
    return area, perim


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) in seen:
            continue
        area, perimeter = getAttributes(grid, i, j, grid[i][j])
        totalPrice += perimeter * area

print(totalPrice)
