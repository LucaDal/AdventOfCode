import re

def check(info: dict,phase):
    for i in range(len(info)):
        if len(info[i]) != phase:
            info[i].append(info[i][phase-2])

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

seeds = list(map(int, re.findall('\d+', lines[0])))

info = [[seed] for seed in seeds]

phase = 0
is_mapping = False
for line,raw in zip(lines, range(len(lines))):
    if line != '' and line[0].isdigit():
        is_mapping = True
        values = list(map(int,re.findall('\d+', line))) # destination, source, range

        for i in range(len(seeds)):
            if info[i][phase-2] >= values[1] and info[i][phase-2] <= values[1]+values[2]:
                info[i].append(values[0] + (info[i][phase-2] - values[1]))

    if line != '' and line[0].isalpha():
        phase += 1 
    if len(line) == 0 or (raw == len(lines)-1): 
        if is_mapping:
            check(info,phase)
            is_mapping = False

print(min(info[i][-1] for i in range(len(info))))