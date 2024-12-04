import sys
input = sys.stdin

total = 0
preface = 'mul('
dontDirective = 'don\'t()'
doDirective = 'do()'

class State():
    PREFACE = 1,
    FIRSTNUM = 2,
    SECONDNUM = 3

active = True

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
        if len(line) - idx > 4 and line[idx:idx+4] == doDirective:
            active = True
        
        if len(line) - idx > 7 and line[idx:idx+7] == dontDirective:
            active = False
            prefaceIdx = 0
            state = State.PREFACE
            first = ''
            second = ''

        
        if(active):
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