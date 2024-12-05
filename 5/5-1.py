import sys
input = sys.stdin
from collections import defaultdict

ordering = defaultdict(list)
total = 0

# Get rules
while True:
    line = input.readline()
    if line == "" or line=="\n":
        break

    [ first, second ] = line.split("|")
    first = int(first)
    second = int(second)
    ordering[second].append(first)

# Get Updates
while True:
    line = input.readline()
    if line == "":
        break

    rules = list(map(int, line.split(",")))
    previous = set()
    cannotExist = set()
    addVal = True
    for rule in rules:
        if rule in cannotExist:
            # Breaks a rule
            addVal = False
            break
        if rule in ordering:
            for order in ordering[rule]:
                if order not in previous:
                    cannotExist.add(order)
        previous.add(rule)
    
    if addVal:
        total += rules[len(rules) // 2]

print(total)