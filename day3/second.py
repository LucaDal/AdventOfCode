def check(raw,index,symbols):
    for y in range(raw-1, raw+2):
        for x in range(index-1, index+2):
            if symbols.get(y) is not None:
                if x in symbols.get(y):
                    return (True,y,x)
    return (False,-1,-1)

with open('input.txt','r') as f:
    lines = f.read().splitlines()

symbols = {} #line, index
motor_parts = []

for line,raw in zip(lines, range(len(lines))):
    line_symbols= []
    for index in range(len(line)):
        if line[index] == '*':
            line_symbols.append(index)
    if len(line_symbols) != 0:
        symbols[raw] = line_symbols

for line,raw in zip(lines, range(len(lines))):
    value = ''
    is_part = False
    temp_raw = -1
    temp_col = -1
    for index in range(len(line)):
        if line[index].isnumeric():
            if is_part is False:
                is_part,temp_raw,temp_col = check(raw,index,symbols)
            value += line[index]
        else:
            if is_part:
                motor_parts.append((int(value),temp_raw,temp_col))
                is_part = False
            value = ''
        if index == len(line)-1 and is_part:
            motor_parts.append((int(value),temp_raw,temp_col))

dict_gear = {}
for gear in motor_parts:
    cord = str(gear[1])+','+str(gear[2])
    if dict_gear.get(cord) is not None:
        dict_gear.get(cord).append(gear[0])
    else:
        dict_gear[cord] = [gear[0]]

gears = []
for key in dict_gear.keys():
    if len(dict_gear.get(key)) == 2:
        gears.append(dict_gear.get(key)[0]*dict_gear.get(key)[1])

print(sum(gears))