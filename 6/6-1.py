import sys
input = sys.stdin
lines = input.read().split('\n')
loc = (-1,-1)
for i in range(len(lines)):
    if lines[i].find('^') != -1:
        loc = (i, lines[i].find('^'))
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

def inGrid(loc):
    return  loc[0] >= 0 and \
            loc[0] < len(lines) and \
            loc[1] >= 0 and \
            loc[1] < len(lines[0])

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

direction = Direction.UP
visited = set()
visited.add(loc)

while True:
    newY, newX = getStep(loc, direction)
    if not inGrid((newY, newX)):
        break
    if lines[newY][newX] == '.' or lines[newY][newX] == '^':
        loc = (newY, newX)
        if loc not in visited:
            visited.add(loc)
    else:
        direction = Direction.NEW_DIRECTION[direction]

print(len(visited))