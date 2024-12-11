import sys
input = sys.stdin

stones = input.read().split(' ')

# 0 -> 1
# Even number of digits -> Split in half
# Else -> * 2024

for i in range(25):
    newStones = []
    for stone in stones:
        if stone == '0':
            newStones.append('1')
            continue
        if len(stone) % 2 == 0:
            first = stone[:len(stone) // 2]
            second = stone[len(stone) // 2:]
            newStones.append(str(int(first)))
            newStones.append(str(int(second)))
        else:
            newStones.append(str(int(stone) * 2024))
    stones = newStones

print(len(stones))