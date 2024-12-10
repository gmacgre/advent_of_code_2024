import sys
input = sys.stdin
items = list(map(int, list(input.read())))

class AmpFile:
    def __init__(self, id, idx, size):
        self.id = id
        self.size = size
        self.idx = idx

    def __str__(self):
        return f'{self.id}::{self.size} slots'
    
    def __repr__(self):
        return f'{self.id}::{self.size} slots'

class Gap:
    def __init__(self, idx, size):
        self.idx = idx
        self.size = size

    def __repr__(self):
        return f'{self.idx}::{self.size} slots'

memory = []
files = []
gaps = []

isFile = True
id = 0
idx = 0
for item in items:
    for i in range(item):
        if isFile:
            memory.append(id)
        else:
            memory.append('.')
    if isFile:
        files.append(AmpFile(id, idx, item))
    else:
        if item > 0:
            gaps.append(Gap(idx,item))
    idx += item
    isFile = not isFile
    if isFile:
        id += 1

for i in range(len(files) - 1, 0, -1):
    toMove = files[i]
    minSize = toMove.size
    for i in range(len(gaps)):
        if gaps[i].size < minSize:
            continue

        for j in range(minSize):
            memory[toMove.idx + j] = '.'
            memory[gaps[i].idx + j] = toMove.id
        
        gaps[i].idx += toMove.size
        gaps[i].size -= toMove.size
        break

total = 0
for idx in range(len(memory)):
    if memory[idx] == '.':
        continue
    total += idx * memory[idx]
    idx += 1

print(total)

# There is a bug here somewhere, I don't know where to fix it for now :(