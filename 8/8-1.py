import sys
input = sys.stdin
lines = list(map(list, input.read().split('\n')))

antennae = {}

max_i = len(lines)
max_j = len(lines[0])

def isValidAntinode(antinode):
    if antinode[0] >= max_i or antinode[0] < 0:
        return False
    if antinode[1] >= max_j or antinode[1] < 0:
        return False
    return True

def makeAntinode(base, shifter):
    return ((2 * base[0]) - shifter[0], (2 * base[1]) - shifter[1])

for i in range(max_i):
    for j in range(max_j):
        if lines[i][j] != '.':
            if lines[i][j] not in antennae:
                antennae[lines[i][j]] = []
            antennae[lines[i][j]].append((i,j))

antinodes = set()
for groupKey in antennae.keys():
    group = antennae[groupKey]
    if len(group) == 1:
        continue
    for i in range(len(group) - 1):
        first = group[i]
        for j in range(i + 1,len(group)):
            second = group[j]
            antinode = makeAntinode(first, second)
            if isValidAntinode(antinode):
                antinodes.add(antinode)
            antinode = makeAntinode(second, first)
            if isValidAntinode(antinode):
                antinodes.add(antinode)

print(len(antinodes))