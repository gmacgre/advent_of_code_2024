import sys
import math
from datetime import datetime
import heapq as hq
input = sys.stdin
maze = list(map(list, input.read().split('\n')))
startLoc = (-1,-1)
startFound = False
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'S':
            startLoc = (i,j)
            startFound = True
            break
    if startFound:
        break
class Direction():
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    MODIFIERS = [
        (-1,0),
        (0,1),
        (1,0),
        (0,-1),
    ]
    TURNS = [
        [RIGHT, LEFT],
        [UP, DOWN],
        [RIGHT, LEFT],
        [UP, DOWN]
    ]


def searchMaze(maze, currLoc):
    alreadySolved = math.inf
    reviewed = set()
    pq = []
    hq.heappush(pq, (0, (currLoc, Direction.RIGHT)))
    while len(pq) > 0:
        score, locDir = hq.heappop(pq)
        if locDir in reviewed:
            continue
        reviewed.add(locDir)
        location, dir = locDir
        if  score >= alreadySolved or \
            maze[location[0]][location[1]] == '#':
            continue
        if maze[location[0]][location[1]] == 'E':
            alreadySolved = score
            continue
        if maze[location[0]][location[1]] == '.' or maze[location[0]][location[1]] == 'S':
            mods = Direction.MODIFIERS[dir]
            hq.heappush(pq, (score + 1, ((location[0] + mods[0], location[1] + mods[1]), dir)))
        for turn in Direction.TURNS[dir]:
            hq.heappush(pq,(score + 1000, (location, turn)))
    return alreadySolved

start = datetime.now()
print(searchMaze(maze, startLoc))
print(f'Solved in {datetime.now() - start}')