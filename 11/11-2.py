import sys
input = sys.stdin

stones = input.read().split(' ')

calculated = {}

def splitNumber(number):
    left = number[:len(number) // 2]
    right = number[len(number) // 2:]
    return str(int(left)), str(int(right))

def calculateStoneCount(number, blinksLeft):
    if blinksLeft == 0:
        return 1
    if (number, blinksLeft) in calculated:
        return calculated[(number, blinksLeft)]
    
    if number == '0':
        calculated[(number, blinksLeft)] = calculateStoneCount('1', blinksLeft - 1)
    elif len(number) % 2 == 0:
        left, right = splitNumber(number)
        leftCount = calculateStoneCount(left, blinksLeft - 1)
        rightCount = calculateStoneCount(right, blinksLeft - 1)
        calculated[(number, blinksLeft)] = leftCount + rightCount    
    else:
        calculated[(number, blinksLeft)] = calculateStoneCount(str(int(number) * 2024), blinksLeft - 1)

    return calculated[(number, blinksLeft)]

total = 0

for stone in stones:
    total += calculateStoneCount(stone, 75)

print(total)