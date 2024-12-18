import sys
import heapq as hq
input = sys.stdin
dimension = 70
# dimension = 6
byteAmount = 1024
# byteAmount = 12
mods = [(-1, 0), (1, 0), (0, -1), (0, 1)]
listBytes = list(map(lambda x: list(map(int, x.split(','))),input.read().split('\n')))
bytes = set()
for i in range(byteAmount):
    pair = listBytes[i]
    bytes.add((pair[0], pair[1]))

reviewed = set()
pq = []
hq.heappush(pq, (0, (0, 0)))
while len(pq) > 0:
    steps, location = hq.heappop(pq)
    if location in reviewed:
        continue
    if location == (dimension, dimension):
        print(steps)
    reviewed.add(location)
    for mod in mods:
        cursor = (location[0] + mod[0], location[1] + mod[1])
        if cursor in bytes:
            continue
        if cursor[0] < 0 or cursor[0] > dimension or cursor[1] < 0 or cursor[1] > dimension:
            continue
        hq.heappush(pq, (steps + 1, cursor))

