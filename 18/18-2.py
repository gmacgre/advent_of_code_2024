import sys
import heapq as hq
input = sys.stdin
dimension = 70
# dimension = 6
mods = [(-1, 0), (1, 0), (0, -1), (0, 1)]
listBytes = list(map(lambda x: list(map(int, x.split(','))),input.read().split('\n')))

def findEnd(dimension, bytes, mods):
    reviewed = set()
    pq = []
    hq.heappush(pq, (0, (0, 0)))
    while len(pq) > 0:
        steps, location = hq.heappop(pq)
        if location in reviewed:
            continue
        if location == (dimension, dimension):
            return steps
        reviewed.add(location)
        for mod in mods:
            cursor = (location[0] + mod[0], location[1] + mod[1])
            if cursor in bytes:
                continue
            if cursor[0] < 0 or cursor[0] > dimension or cursor[1] < 0 or cursor[1] > dimension:
                continue
            hq.heappush(pq, (steps + 1, cursor))
    return None

byteQuantity = len(listBytes) // 2
upper = len(listBytes)
lower = 0
checked = set()
while True:
    print(byteQuantity)
    checked.add(byteQuantity)
    bytes = set()
    for i in range(byteQuantity):
        pair = listBytes[i]
        bytes.add((pair[0], pair[1]))
    if findEnd(dimension, bytes, mods) is not None:
        #Path Still around, go to upper bucket
        lower = byteQuantity
    else:
        #No path, go to lower bucket
        upper = byteQuantity
    if lower == upper - 1:
        print(listBytes[lower])
        break
    byteQuantity = (upper + lower) // 2