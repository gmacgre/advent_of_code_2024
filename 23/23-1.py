import sys
input = sys.stdin
lines = input.read().split('\n')
network = {}
possible = []
for conn in lines:
    src, dest = conn.split('-')
    
    if src not in network:
        network[src] = []
    if dest not in network:
        network[dest] = []
    network[src].append(dest)
    network[dest].append(src)
    for link in network[src]:
        if link in network[dest]:
            possible.append((link, src, dest))

final = list(filter(lambda x: any(list(map(lambda y: y.startswith('t'), x))), possible))

print(len(final))
    