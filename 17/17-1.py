import sys
input = sys.stdin
class Instructions():
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7

regInput, progInput = input.read().split('\n\n')
regAInput, regBInput, regCInput = regInput.split('\n')
program = list(map(int, progInput.split(': ')[1].split(',')))
regs = {
    'A': int(regAInput.split(': ')[1]),
    'B': int(regBInput.split(': ')[1]),
    'C': int(regCInput.split(': ')[1]),
}
intrptr = 0
outputs = []

def getCombo(regs, op):
    if op < 4:
        return op
    match op:
        case 4:
            return regs['A']
        case 5:
            return regs['B']
        case 6:
            return regs['C']
    return 'OP is 7, reserved'

while intrptr >= 0 and intrptr < len(program) - 1:
    code = program[intrptr]
    operand = program[intrptr + 1]
    match code:
        case Instructions.ADV:
            regs['A'] = regs['A'] // 2 ** getCombo(regs, operand)
        case Instructions.BXL:
            regs['B'] = regs['B'] ^ operand
        case Instructions.BST:
            regs['B'] = getCombo(regs, operand) % 8
        case Instructions.JNZ:
            if regs['A'] != 0:
                intrptr = operand - 2 # 2 For inc offset
        case Instructions.BXC:
            regs['B'] = regs['B'] ^ regs['C']
        case Instructions.OUT:
            outputs.append(str(getCombo(regs, operand) % 8))
        case Instructions.BDV:
            regs['B'] = regs['A'] // 2 ** getCombo(regs, operand)
        case Instructions.CDV:
            regs['C'] = regs['A'] // 2 ** getCombo(regs, operand)
    intrptr += 2
print(','.join(outputs))