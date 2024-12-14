import sys
input = sys.stdin

lines = input.read().split('\n')
bots = []
for line in lines:
    p, v = line.split(' ')
    p = p.split('=')[1]
    v = v.split('=')[1]
    p_x, p_y = list(map(int,p.split(',')))
    v_x, v_y = list(map(int,v.split(',')))
    bots.append({
        'pos': (p_x, p_y),
        'vel': (v_x, v_y)
    })

mapWidth = 101
mapHeight = 103
secondCount = 100

buckets = [0] * 4

for bot in bots:
    pos = bot['pos']
    vel = bot['vel']
    new_x = (pos[0] + (vel[0] * secondCount)) % mapWidth
    new_y = (pos[1] + (vel[1] * secondCount)) % mapHeight
    bucketId = 0
    if new_x == mapWidth // 2 or new_y == mapHeight // 2:
        continue
    if new_x > mapWidth // 2:
        bucketId += 1
    if new_y > mapHeight // 2:
        bucketId += 2
    buckets[bucketId] += 1 

total = 1
for bucket in buckets:
    total *= bucket

print(total)