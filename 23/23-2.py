import sys
input = sys.stdin
lines = input.read().split('\n')
network = {}
netSet = {}
possible = []
for conn in lines:
    src, dest = conn.split('-')
    if src not in network:
        network[src] = []
        netSet[src] = set()
    if dest not in network:
        network[dest] = []
        netSet[dest] = set()

    network[src].append(dest)
    network[dest].append(src)
    netSet[src].add(dest)
    netSet[dest].add(src)
    for link in network[src]:
        if link in netSet[dest]:
            possible.append((link, src, dest))

def buildClique(sub_clique, network, netSet):
    new_clique = sub_clique.copy()
    node = new_clique[0]
    for connection in network[node]:
        for checkNode in sub_clique:
            if connection not in netSet[checkNode]:
                break
        else: 
            new_clique.append(connection)
            break
    if len(new_clique) > len(sub_clique):
        return buildClique(new_clique, network, netSet)
    return new_clique 

largest_clique = None
for grouping in possible:
    clique = buildClique(list(grouping), network, netSet)
    if largest_clique is None or len(largest_clique) < len(clique):
        print(clique)
        largest_clique = clique
largest_clique.sort()
print(','.join(largest_clique))

    