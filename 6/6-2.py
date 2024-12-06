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

def runPath(path, loc, dir):
    direction = dir
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
direction = Direction.UP
start_y, start_x = loc[0], loc[1]
visited = set()
while True:
    newY, newX = getStep(loc, direction)
    if not inGrid((newY, newX), lines):
        break
    if lines[newY][newX] == '^':
        loc = (newY, newX)
        continue
    if (newY, newX) in visited:
        loc = (newY, newX)
        continue
    if lines[newY][newX] == '.':
        lines[newY][newX] = '#'
        if runPath(lines, (start_y, start_x), Direction.UP):
            count += 1
        loc = (newY, newX)
        visited.add(loc)
        lines[newY][newX] = '.'
    else:
        direction = Direction.NEW_DIRECTION[direction]

p1_end = datetime.now()
print(f'Found {count} in {p1_end - p1_start}')