import re
with open('input.txt','r') as f:
    lines = f.read().splitlines()

times = list(re.findall(r"\d+", lines[0]))
times = [int(''.join(times[:]))]
distances = list(re.findall(r"\d+", lines[1]))
distances = [int(''.join(distances[:]))]

print(times,distances)
ways_to_win = []
for time, distance in zip(times,distances):
    counter : int = 0
    for millisecond_push in range(time+1):
        distances_from_push = millisecond_push * (time - millisecond_push)
        if distances_from_push > distance:
            counter += 1
    ways_to_win.append(counter)

print(ways_to_win[0])