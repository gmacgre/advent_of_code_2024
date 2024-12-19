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
    totalCombinations = 0
    if d in pats:
        totalCombinations += 1
    toUse = long if long < len(d) else len(d)
    for i in range(toUse + 1):
        if d[:i] in pats:  
            totalCombinations += canBuild(d[i:], long, pats, solveable)
    solveable[d] = totalCombinations
    return totalCombinations

total = 0
solveable = {}
for d in designs:
    val = canBuild(d, longest, patterns, solveable)
    total += val
print(total)