import sys
input = sys.stdin
startVals, conns = input.read().split('\n\n')
startVals = startVals.split('\n')
conns = conns.split('\n')
states = {}
toMeld = {}
for val in startVals:
    node, value = val.split(': ')
    states[node] = True if value == '1' else False

def getResult(first, second, op):
    match op:
        case 'AND':
            return first and second
        case 'XOR':
            return first ^ second
        case 'OR':
            return first or second

while len(conns) > 0:
    conn = conns.pop(0)
    combination, result = conn.split(' -> ')
    first, op, second = combination.split(' ')
    if first not in states or second not in states:
        conns.append(conn)
        continue
    res = getResult(states[first], states[second], op)
    states[result] = res
    if result[0] == 'z':
        toMeld[result] = res

toConv = ''
for zKey in reversed(sorted(list(toMeld))):
    toConv += '1' if states[zKey] else '0'
print(int(toConv, 2))