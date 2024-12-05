import sys
input = sys.stdin

target = 'XMAS'
total = 0
wordSearch = []

while True:
    line = input.readline()
    if line == "":
        break
    wordSearch.append(line[:-1])


for i in range(len(wordSearch)):
    for j in range(len(wordSearch[0])):
        if wordSearch[i][j] != target[0]:
            continue

        canUp = (i - 3) >= 0
        canDown = (i + 3) < len(wordSearch)
        canLeft = (j - 3) >= 0 
        canRight = (j + 3) < len(wordSearch[0])

        if canUp:
            total += 1 if (wordSearch[i][j] + wordSearch[i-1][j] + wordSearch[i-2][j] + wordSearch[i-3][j]) == target else 0
        if canDown:
            total += 1 if (wordSearch[i][j] + wordSearch[i+1][j] + wordSearch[i+2][j] + wordSearch[i+3][j]) == target else 0
        if canLeft:
            total += 1 if (wordSearch[i][j-3:j+1])[::-1] == target else 0
        if canRight:
            total += 1 if wordSearch[i][j:j+4] == target else 0
        if canUp and canLeft:
            total += 1 if (wordSearch[i][j] + wordSearch[i-1][j-1] + wordSearch[i-2][j-2] + wordSearch[i-3][j-3]) == target else 0
        if canUp and canRight:
            total += 1 if (wordSearch[i][j] + wordSearch[i-1][j+1] + wordSearch[i-2][j+2] + wordSearch[i-3][j+3]) == target else 0
        if canDown and canLeft:
            total += 1 if (wordSearch[i][j] + wordSearch[i+1][j-1] + wordSearch[i+2][j-2] + wordSearch[i+3][j-3]) == target else 0
        if canDown and canRight:
            total += 1 if (wordSearch[i][j] + wordSearch[i+1][j+1] + wordSearch[i+2][j+2] + wordSearch[i+3][j+3]) == target else 0

print(total)
