#
# A visualizer solution to part 1
#

import os
import sys
input = sys.stdin
sections = input.read().split('\n\n')
warehouse = list(map(list, sections[0].split('\n')))
dirs = { '<': (0,-1), '^': (-1,0), 'v': (1,0), '>': (0,1) }
moves = sections[1]
bot = (0,0)
#Find the bot
for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if warehouse[i][j] == '@':
            bot = (i,j)
            break
    if bot != (0,0):
        break

def canMove(ware, bot, dir):
    checker = bot
    while True:
        checker = (checker[0] + dir[0], checker[1] + dir[1])
        if ware[checker[0]][checker[1]] == '.':
            return True
        elif ware[checker[0]][checker[1]] == '#':
            return False
        
def printWarehouse(ware):
    for line in ware:
        toPrint = ''
        for place in line:
            toPrint += place
        print(toPrint)
    
def getScore(ware):
    total = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == 'O':
                total += (100 * i) + j
    return total
            
        
def moveBot(ware, bot, dir):
    hold  = '.'
    prev = bot   
    cursor = prev
    
    while True:
        cursor = (prev[0] + dir[0], prev[1] + dir[1])
        newHold = ware[prev[0]][prev[1]]
        ware[prev[0]][prev[1]] = hold
        hold = newHold
        prev = cursor
        if ware[cursor[0]][cursor[1]] == '#' or ware[cursor[0]][cursor[1]] == '.':
            break
    ware[cursor[0]][cursor[1]] = hold

step = 1
length = len(moves)
for character in moves:
    if character == '\n':
        continue
    dir = dirs[character]
    if canMove(warehouse, bot, dir):
        moveBot(warehouse, bot, dir)
        bot = (bot[0] + dir[0], bot[1] + dir[1])
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Step {step}: {character} (of {length})')
    print('----------------------------------------------------------')
    printWarehouse(warehouse)
    print('----------------------------------------------------------')
    print(f'Score: {getScore(warehouse)}')
    step += 1

