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
secondCount = 0
while True:
    locs = set()
    copy = False
    for bot in bots:
        pos = bot['pos']
        vel = bot['vel']
        new_x = (pos[0] + (vel[0] * secondCount)) % mapWidth
        new_y = (pos[1] + (vel[1] * secondCount)) % mapHeight
        if (new_x, new_y) in locs:
            copy = True
            break
        locs.add((new_x, new_y))

    if not copy:
        break
    secondCount += 1

print(secondCount)