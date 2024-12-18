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
targProg = progInput.split(': ')[1]
program = list(map(int, targProg.split(',')))
regs = {
    'A': int(regAInput.split(': ')[1]),
    'B': int(regBInput.split(': ')[1]),
    'C': int(regCInput.split(': ')[1]),
}


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

def runProg(regs, program):
    intrptr = 0
    outputs = []
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
                outputs.append(getCombo(regs, operand) % 8)
            case Instructions.BDV:
                regs['B'] = regs['A'] // 2 ** getCombo(regs, operand)
            case Instructions.CDV:
                regs['C'] = regs['A'] // 2 ** getCombo(regs, operand)
        intrptr += 2
    return outputs

def findCode(regs, program):
    q = [(len(program) - 1, 0)] # program always ends with zero
    while len(q) > 0:
        i, opcode = q.pop(0)
        for op in range(8):
            reg_val = (opcode << 3) + op
            regs['A'] = reg_val
            regs['B'] = 0
            regs['C'] = 0
            if runProg(regs, program) == program[i:]:
                if i == 0: return reg_val
                q.append((i - 1, reg_val))
    return None

print(findCode(regs, program))
