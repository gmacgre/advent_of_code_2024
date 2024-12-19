import sys
input = sys.stdin
patterns = {}
listPat, designs = input.read().split('\n\n')
listPat = listPat.split(', ')
designs = designs.split('\n')
longest = 0
for p in listPat:
    if len(p) > longest:
        longest = len(p)
    patterns[p] = 1

def canBuild(d, long, pats, solveable):
    if d in solveable:
        return solveable[d]
    if d == '':
        return True
    for i in range(long, 0, -1):
        if d[0:i] in pats:
            if canBuild(d[i:], long, pats, solveable):
                solveable[d] = True
                return True
    solveable[d] = False
    return False

total = 0
solveable = {}
for d in designs:
    if canBuild(d, longest, patterns, solveable):
        total += 1
print(total)