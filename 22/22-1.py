import sys
input = sys.stdin
lines = list(map(int,input.read().split('\n')))

def mix(input: int, specialNum: int) -> int:
    return specialNum ^ input

def prune(specialNum: int) -> int:
    return specialNum % 16777216

def getNextNumber(currPrice: int) -> int:
    newPrice = currPrice * 64
    newPrice = mix(newPrice, currPrice)
    newPrice = prune(newPrice)
    other = newPrice // 32
    newPrice = mix(other, newPrice)
    newPrice = prune(newPrice)
    other = newPrice * 2048
    newPrice = mix(other, newPrice)
    newPrice = prune(newPrice)
    return newPrice

def getNumber(currPrice: int, iterations=2000) -> int:
    for i in range(iterations):
        currPrice = getNextNumber(currPrice)
    return currPrice

    
print(sum([getNumber(i) for i in lines]))