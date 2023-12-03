def check(raw,index,symbols):
    for y in range(raw-1, raw+2):
        for x in range(index-1, index+2):
            if symbols.get(y) is not None:
                if x in symbols.get(y):
                    return True
    return False

with open('input.txt','r') as f:
    lines = f.read().splitlines()

symbols = {} #line, index
motor_parts = []

for line,raw in zip(lines, range(len(lines))):
    line_symbols= []
    for index in range(len(line)):
        if not line[index].isnumeric() and line[index] != '.':
            line_symbols.append(index)
    if len(line_symbols) != 0:
        symbols[raw] = line_symbols

for line,raw in zip(lines, range(len(lines))):
    value = ''
    is_part = False
    for index in range(len(line)):
        if line[index].isnumeric():
            if is_part is False:
                is_part = check(raw,index,symbols)
            value += line[index]
        else:
            if is_part:
                motor_parts.append(int(value))
                is_part = False
            value = ''
        if index == len(line)-1 and is_part:
            motor_parts.append(int(value))

print(sum(motor_parts))