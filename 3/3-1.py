import sys
input = sys.stdin

total = 0
preface = 'mul('

class State():
    PREFACE = 1,
    FIRSTNUM = 2,
    SECONDNUM = 3

while True:
    line = input.readline()
    if line == "":
        break

    lineTotal = 0
    idx = 0
    prefaceIdx = 0
    state = State.PREFACE
    first = ''
    second = ''

    while idx < len(line):

        match state:
            case State.PREFACE:
                if line[idx] == preface[prefaceIdx]:
                    if prefaceIdx == 0:
                        check = idx
                    prefaceIdx += 1
                    if prefaceIdx >= len(preface):
                        prefaceIdx = 0
                        state = State.FIRSTNUM
                else:
                    prefaceIdx = 0

            case State.FIRSTNUM:
                if line[idx].isdigit():
                    first += line[idx]
                elif line[idx] == ',':
                    state = State.SECONDNUM
                else:
                    first = ''
                    state = State.PREFACE
                
            
            case State.SECONDNUM:
                if line[idx].isdigit():
                    second += line[idx]
                elif line[idx] == ')':
                    lineTotal += int(first) * int(second)
                    second = ''
                    first = ''
                    state = State.PREFACE
                else:
                    second = ''
                    first = ''
                    state = State.PREFACE

        idx += 1


    total += lineTotal

print(total)

#Add Post-Input code here