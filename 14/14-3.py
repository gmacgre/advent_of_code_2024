#
# An alternate, slower way of solving part 2 using DFS- since appearantly that's how the tree is defined is NOT when there are no double locations
#

import sys
from datetime import datetime
input = sys.stdin
lines = input.read().split('\n')
bots = []

start = datetime.now()

def wipeBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = '.'

def getSize(board, i, j, visited):
    if (i,j) in visited:
        return 0
    visited.add((i,j))
    if board[i][j] != 'X':
        return 0
    
    toRet = 1
    if i > 0:
        toRet += getSize(board, i-1, j, visited)
    if i < len(board) - 1:
        toRet += getSize(board, i+1, j, visited)
    if j > 0:
        toRet += getSize(board, i, j-1, visited)
    if j < len(board[0]) - 1:
        toRet += getSize(board, i, j+1, visited)
    
    return toRet
    
for line in lines:
    p, v = line.split(' ')
    p = p.split('=')[1]
    v = v.split('=')[1]
    p_x, p_y = list(map(int,p.split(',')))
    v_x, v_y = list(map(int,v.split(',')))
    bots.append({
        'pos': (p_x, p_y),
        'vel': (v_x, v_y)
    })

mapWidth = 101
mapHeight = 103
secondCount = 0
threshold = 30
board = []
for i in range(mapWidth):
    board.append(['.'] * mapHeight)

while True:
    visited = set()
    shouldBreak = False
    for bot in bots:
        pos = bot['pos']
        vel = bot['vel']
        new_x = (pos[0] + (vel[0] * secondCount)) % mapWidth
        new_y = (pos[1] + (vel[1] * secondCount)) % mapHeight
        board[new_x][new_y] = 'X'
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                continue
            if getSize(board, i, j, visited) > threshold:
                shouldBreak = True
    
    if shouldBreak:
        break
    wipeBoard(board)    
    secondCount += 1

print(secondCount)