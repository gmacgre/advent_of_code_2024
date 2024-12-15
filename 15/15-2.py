import sys
input = sys.stdin
verbose = False
def printWarehouse(ware):
    for line in ware:
        toPrint = ''
        for place in line:
            toPrint += place
        print(toPrint)

def convertWarehouse(ware):
    toRet = []
    for line in ware:
        strLine = ''
        for place in line:
            strLine += addChars[place]
        toRet.append(list(strLine))
    return toRet

sections = input.read().split('\n\n')
warehouse = list(map(list, sections[0].split('\n')))
dirs = { '<': (0,-1), '^': (-1,0), 'v': (1,0), '>': (0,1) }
addChars = { '#': '##', '.': '..', 'O': '[]', '@': '@.',}
moves = sections[1]
bot = (0,0)
warehouse = convertWarehouse(warehouse)
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
    needChecks = [bot]
    while len(needChecks) > 0:
        newChecks = set()
        for check in needChecks:
            checker = (check[0] + dir[0], check[1] + dir[1])
            if ware[checker[0]][checker[1]] == '.':
                continue
            elif ware[checker[0]][checker[1]] == '#':
                return False
            newChecks.add(checker)
            if dir == dirs['<'] or dir == dirs['>']:
                continue
            if ware[checker[0]][checker[1]] == '[':
                newChecks.add((checker[0], checker[1] + 1))
            if ware[checker[0]][checker[1]] == ']':
                newChecks.add((checker[0], checker[1] - 1))
        needChecks = newChecks
    return True

def moveBot(ware, bot, dir):
    if dir == dirs['<'] or dir == dirs['>']:
        moveBotHorizontal(ware, bot, dir)
    else:
        moveBotVertical(ware, bot, dir)

def moveBotVertical(ware, bot, dir):
    toMove = set()
    toPush = []
    toPush.append((bot, '.'))
    while len(toPush) > 0:
        newPush = []
        for val in toPush:
            loc, prev = val
            nextCoords = (loc[0] + dir[0], loc[1] + dir[1])
            if ware[loc[0]][loc[1]] != '.':
                newPush.append((nextCoords, ware[loc[0]][loc[1]]))
                if ware[loc[0]][loc[1]] == '[':
                    nextCoords = (loc[0], loc[1] + 1)
                    if nextCoords not in toMove:
                        newPush.append((nextCoords, '.'))
                        toMove.add(nextCoords)
                elif ware[loc[0]][loc[1]] == ']':
                    nextCoords = (loc[0], loc[1] - 1)
                    if nextCoords not in toMove:
                        newPush.append((nextCoords, '.'))
                        toMove.add(nextCoords)
            toMove.add(loc)
            ware[loc[0]][loc[1]] = prev
        toPush = newPush

def moveBotHorizontal(ware, bot, dir):
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
for character in moves:
    if character == '\n':
        continue
    dir = dirs[character]
    if canMove(warehouse, bot, dir):
        moveBot(warehouse, bot, dir)
        bot = (bot[0] + dir[0], bot[1] + dir[1])
    if verbose:
        print(f'Step {step}: {character}')
        printWarehouse(warehouse)
    step += 1
    

total = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if warehouse[i][j] == '[':
            total += (100 * i) + j

print(total)