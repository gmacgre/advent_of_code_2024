import sys
input = sys.stdin

first = []
second = {}

while True:
    line = input.readline()
    #interpret line
    if line == "":
        break

    left, right = line.split('   ')
    right = right[:len(right) - 1]
    first.append(int(left))
    right = int(right)
    if right in second:
        second[right] += 1
    else:
        second[right] = 1

totalSimilarity = 0

for num in first:
    if num in second:
        totalSimilarity += num * second[num]


print(totalSimilarity)