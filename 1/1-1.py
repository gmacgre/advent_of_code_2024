import sys
input = sys.stdin

first = []
second = []

while True:
    line = input.readline()
    if line == "":
        break

    left, right = line.split('   ')
    right = right[:len(right) - 1]
    first.append(int(left))
    second.append(int(right))

first.sort()
second.sort()

totalDistance = 0

for i in range(len(first)):
    totalDistance += max(first[i],second[i]) - min(first[i],second[i])
    
print(totalDistance)