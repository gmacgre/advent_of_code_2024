import sys
input = sys.stdin

total = 0
wordSearch = []

while True:
    line = input.readline()
    if line == "":
        break
    wordSearch.append(line[:-1])

def checkSquare(i,j):
    letter = wordSearch[i-1][j-1]
    if letter == 'M':
        if wordSearch[i+1][j-1] == 'M' and \
           wordSearch[i-1][j+1] == 'S' and \
           wordSearch[i+1][j+1] == 'S' :
            return True
        
        if wordSearch[i+1][j-1] == 'S' and \
           wordSearch[i-1][j+1] == 'M' and \
           wordSearch[i+1][j+1] == 'S' :
            return True
    
    if letter == 'S':
        if wordSearch[i+1][j-1] == 'S' and \
           wordSearch[i-1][j+1] == 'M' and \
           wordSearch[i+1][j+1] == 'M' :
            return True
        
        if wordSearch[i+1][j-1] == 'M' and \
           wordSearch[i-1][j+1] == 'S' and \
           wordSearch[i+1][j+1] == 'M' :
            return True


for i in range(1,len(wordSearch)-1):
    for j in range(1,len(wordSearch[0])-1):
        if wordSearch[i][j] != 'A':
            continue
        if checkSquare(i,j):
            total += 1

print(total)
