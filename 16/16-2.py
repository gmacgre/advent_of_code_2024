import sys
import math
from datetime import datetime
import heapq as hq
input = sys.stdin
maze = list(map(list, input.read().split('\n')))
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
    DIRECTIONS = [
        UP, RIGHT, DOWN, LEFT
    ]
              
def findNode(maze, target):
    startLoc = (-1,-1)
    startFound = False
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == target:
                startLoc = (i,j)
                startFound = True
                break
        if startFound:
            break
    return startLoc

scoreHold = {}
prevNodes = {}

def addNodes(prevs, checker, totals):
    if checker not in prevs:
        return
    totals.add((checker[0], checker[1]))
    for prev in prevs[checker]:
        addNodes(prevs, prev, totals)

def searchMaze(maze, currLoc):
    alreadySolved = math.inf
    reviewed = set()
    pq = []
    hq.heappush(pq, (0, (currLoc[0], currLoc[1], Direction.RIGHT, -1, -1, -1)))
    while len(pq) > 0:
        score, locAndSrc = hq.heappop(pq)
        y, x, dir, s_y, s_x, s_d = locAndSrc
        locDir = (y, x, dir)
        src = (s_y, s_x, s_d)
        if locDir in reviewed:
            if score == scoreHold[locDir]:
                prevNodes[locDir].append(src)
            continue
        reviewed.add(locDir)
        scoreHold[locDir] = score
        prevNodes[locDir] = [src]
        if  score > alreadySolved or \
            maze[y][x] == '#':
            continue
        if maze[y][x] == 'E':
            alreadySolved = score
            continue
        if maze[y][x] == '.' or maze[y][x] == 'S':
            mods = Direction.MODIFIERS[dir]
            hq.heappush(pq, (score + 1, (y + mods[0], x + mods[1], dir, y, x, dir)))
        for turn in Direction.TURNS[dir]:
            hq.heappush(pq,(score + 1000, (y, x, turn, y, x, dir)))

    endLoc = findNode(maze, 'E')
    totalNodes = set()
    for dir in Direction.DIRECTIONS:
        checker = (endLoc[0], endLoc[1], dir)
        addNodes(prevNodes, checker, totalNodes)
    return len(totalNodes)


start = datetime.now()
print(searchMaze(maze, findNode(maze, 'S')))
print(f'Solved in {datetime.now() - start}')