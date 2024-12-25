import sys
input = sys.stdin
parts = input.read().split('\n\n')
keys = []
locks = []
for part in parts:
    grid = list(map(list, part.split('\n')))
    format = []
    for j in range(len(grid[0])):
        depth = -1
        for i in range(len(grid)):
            if grid[i][j] == '#':
                depth += 1
        format.append(depth)
    format = tuple(format)
    locks.append(format) if grid[0][0] == '#' else keys.append(format)

count = 0
def canFit(lock, key):
    for i in range(len(lock)):
        if lock[i] + key[i] > 5:
            return False
    return True


for lock in locks:
    for key in keys:
        if canFit(lock, key):
            count += 1

print(count)