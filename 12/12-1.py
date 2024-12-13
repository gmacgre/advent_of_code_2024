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

def getAttributes(grid, i, j, target):
    if (i,j) in seen:
        return 0, 0
    seen.add((i,j))
    area = 1
    perim = 0
    for dir in directions:
        if inScope(grid, i+dir[0], j+dir[1]) and grid[i+dir[0]][j+dir[1]] == target:
            newArea, newPerim = getAttributes(grid, i+dir[0], j+dir[1], target)
            area += newArea
            perim += newPerim
        else: #Edge or line with another
            perim += 1
    
    return area, perim


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) in seen:
            continue
        perimeter, area = getAttributes(grid, i, j, grid[i][j])
        totalPrice += perimeter * area

print(totalPrice)
