import sys
input = sys.stdin
from datetime import datetime
lines = input.read().split('\n')
for i in range(len(lines)):
    lines[i] = list(lines[i])
loc = (-1,-1)
for i in range(len(lines)):
    if '^' in lines[i]:
        loc = (i, lines[i].index('^'))
        break

class Direction():
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    NEW_DIRECTION = {
        UP: RIGHT,
        RIGHT: DOWN,
        DOWN: LEFT,
        LEFT: UP
    }

def inGrid(loc,path):
    return  loc[0] >= 0 and \
            loc[0] < len(path) and \
            loc[1] >= 0 and \
            loc[1] < len(path[0])

def getStep(loc, direction):
    match direction:
        case Direction.UP:
            return loc[0] - 1, loc[1]
        case Direction.RIGHT:
            return loc[0], loc[1] + 1
        case Direction.DOWN:
            return loc[0] + 1, loc[1]
        case Direction.LEFT:
            return loc[0], loc[1] - 1

def runPath(path, loc):

    direction = Direction.UP
    loc = (loc[0], loc[1], direction)
    visited = set()
    visited.add(loc)

    while True:
        newY, newX = getStep(loc, direction)
        if not inGrid((newY, newX), path):
            return False
        if path[newY][newX] == '.' or path[newY][newX] == '^':
            loc = (newY, newX, direction)
            if loc not in visited:
                visited.add(loc)
            else:
                return True
        else:
            direction = Direction.NEW_DIRECTION[direction]

count = 0

p1_start = datetime.now()

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == '^' or lines[i][j] == '#':
            continue
        lines[i][j] = '#'
        if runPath(lines, loc):
            count += 1
        lines[i][j] = '.'

p1_end = datetime.now()
print(f'Found XXXX in {p1_end - p1_start}')