import sys
input = sys.stdin
from collections import defaultdict

ordering = defaultdict(list)
invertOrdering = defaultdict(list)
total = 0

def isOrdered(rules):
    previous = set()
    cannotExist = set()
    for rule in rules:
        if rule in cannotExist:
            # Breaks a rule
            return False
        if rule in ordering:
            for order in ordering[rule]:
                if order not in previous:
                    cannotExist.add(order)
        previous.add(rule)
    return True


# Get rules
while True:
    line = input.readline()
    if line == "" or line=="\n":
        break

    [ first, second ] = line.split("|")
    first = int(first)
    second = int(second)
    ordering[second].append(first)
    invertOrdering[first].append(second)
    

toReorder = []
# Get Updates
while True:
    line = input.readline()
    if line == "":
        break
    rules = list(map(int, line.split(",")))
    if not isOrdered(rules):
        toReorder.append(rules)
    


for line in toReorder:
    newLine = []
    dependencies = {}
    alreadyPresent = set()
    possibleDependencies = {}
    for rule in line:
        dependencies[rule] = []
        if rule in ordering:
            for order in ordering[rule]:
                if order in alreadyPresent:
                    dependencies[rule].append(order)
                elif order in possibleDependencies:
                    possibleDependencies[order].append(rule)
                else:
                    possibleDependencies[order] = [ rule ]
        if rule in possibleDependencies: 
            for newDep in possibleDependencies[rule]:
                dependencies[newDep].append(rule)
            del possibleDependencies[rule]
        alreadyPresent.add(rule)
        
    mod_queue = []
    depCounts = {}
    for item in dependencies.keys():
        depCounts[item] = len(dependencies[item])
        if depCounts[item] == 0:
            mod_queue.append(item)

    while(len(mod_queue) != 0):
        toAppend = mod_queue.pop(0)
        newLine.append(toAppend)
        if toAppend in invertOrdering:
            for dep in invertOrdering[toAppend]:
                if dep in depCounts:
                    depCounts[dep] -= 1
                    if depCounts[dep] == 0:
                        mod_queue.append(dep)
    total += newLine[len(newLine) // 2]


print(total)