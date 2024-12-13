import sys
import re
input = sys.stdin
fullMachines = input.read().split('\n\n')
machines = []
def getNumbers(input, addATon):
    input = input.split(': ')[1]
    left, right = input.split(', ')
    left = int(re.split('\+|=', left)[1])
    right = int(re.split('\+|=', right)[1])
    if addATon:
        left += 10000000000000
        right += 10000000000000
    return left, right

for m in fullMachines:
    a_button, b_button, target = m.split('\n')
    newMachine = {
        'a': getNumbers(a_button, False),
        'b': getNumbers(b_button, False),
        'target': getNumbers(target, False)
    }
    machines.append(newMachine)


total = 0
for m in machines:
    target = m['target']
    a_button = m['a']
    b_button =  m['b']
    b = ((a_button[0] * target[1]) - (a_button[1] * target[0])) / ((a_button[0] * b_button[1]) - (a_button[1] * b_button[0]))
    a = (target[0] - b_button[0] * b) / a_button[0]

    # Check if a and b are integers
    if a.is_integer() and b.is_integer():
        total += a * 3 + b

print(int(total))
