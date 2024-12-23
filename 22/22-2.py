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

def getChange(start: int, end: int) -> int:
    return end - start 

def getPriceMap(currPrice: int, iterations=2000) -> int:
    prices = []
    changes = []
    changeMap = {}
    prices.append(currPrice % 10)
    for i in range(iterations):
        currPrice = getNextNumber(currPrice)
        price = currPrice % 10
        changes.append(getChange(prices[-1], price))
        prices.append(price)
        if i > 2:
            toTuple = changes[-4:]
            toTuple = tuple(toTuple)
            if toTuple not in changeMap:
                changeMap[toTuple] = price
    return changeMap

toCheck = set()
mapList = []
for buyer in lines:
    newMap = getPriceMap(buyer)
    mapList.append(newMap)
    for key in newMap.keys():
        toCheck.add(key)
maxBananas = 0
maxKey = -1
for key in toCheck:
    value = sum([0 if key not in priceMap else priceMap[key] for priceMap in mapList])
    if value > maxBananas:
        maxBananas = value
        maxKey = key

print(maxBananas)