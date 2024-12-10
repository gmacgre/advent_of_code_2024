import sys
input = sys.stdin
items = list(map(int, list(input.read())))
memory = []

isFile = True
id = 0
for item in items:
    for i in range(item):
        if isFile:
            memory.append(id)
        else:
            memory.append('.')
    isFile = not isFile
    if isFile:
        id += 1

backIdx = len(memory) - 1
frontIdx = 0

while backIdx > frontIdx:
    if memory[backIdx] == '.':
        backIdx -= 1
        continue
    if memory[frontIdx] != '.':
        frontIdx += 1
        continue

    memory[backIdx], memory[frontIdx] = memory[frontIdx], memory[backIdx]

idx = 0
total = 0
while memory[idx] != '.':
    total += idx * memory[idx]
    idx += 1

print(total)