# https://adventofcode.com/2023/day/6

import re
import math
with open('input.txt','r') as f:
    lines = f.read().splitlines()

times = list(map(int, re.findall(r"\d+", lines[0])))
distances = list(map(int, re.findall(r"\d+", lines[1])))

ways_to_win = []
for time, distance in zip(times,distances):
    counter : int = 0
    for millisecond_push in range(time+1):
        distances_from_push = millisecond_push * (time - millisecond_push)
        if distances_from_push > distance:
            counter += 1
    ways_to_win.append(counter)
print(math.prod(ways_to_win))