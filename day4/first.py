def split(line):
    cards = line.split(':')[1].split('|')
    winning_number = cards[0].split(' ')
    numbers = cards[1].split(' ')
    winning_number = [int(i) for i in winning_number if i != '']
    numbers = [int(i) for i in numbers if i != '']
    return winning_number, numbers


with open('input.txt','r') as f:
    lines = f.read().splitlines()

points = []
for line in lines:
    cards_found = 0
    winning_number, numbers = split(line)
    for number in numbers:
        if number in winning_number:
            cards_found += 1
    if cards_found > 0:
        points.append(2 **(cards_found-1))
print(sum(points))