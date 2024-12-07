import sys
input = sys.stdin
lines = input.read().split('\n')

def modOps(operators):
    for i in range(len(operators) - 1, -1, -1):
        if operators[i] == '+':
            operators[i] = '*'
            return operators, False
        else:
            operators[i] = '+'
    return operators, True

def canCalibrate(target, inputs):
    operators = ['+'] * (len(inputs) - 1)
    while True:
        subTotal = inputs[0]
        for i in range(1, len(inputs)):
            if operators[i-1] == '+':
                subTotal += inputs[i]
            else:
                subTotal *= inputs[i]
        if subTotal == target:
            return True
        operators, shouldBreak = modOps(operators)
        if shouldBreak:
            break
    return False

total = 0
for line in lines:
    [target, inputs] = line.split(": ")
    target = int(target)
    inputs = list(map(int,inputs.split(" ")))
    if canCalibrate(target, inputs):
        total += target

print(total)