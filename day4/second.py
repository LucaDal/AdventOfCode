def split(line):
    cards = line.split(':')[1].split('|')
    winning_number = cards[0].split(' ')
    numbers = cards[1].split(' ')
    winning_number = [int(i) for i in winning_number if i != '']
    numbers = [int(i) for i in numbers if i != '']
    return winning_number, numbers

with open('input.txt','r') as f:
    lines = f.read().splitlines()

winning_cards = {i:0 for i in range(1,len(lines)+1)} #id, quantity

for line, card_id in zip(lines, range(len(lines)+1)):
    cards_found = 0
    copy_cards = []
    winning_number, numbers = split(line)

    winning_cards[card_id+1] = winning_cards.get(card_id+1) + 1

    for number in numbers:
        if number in winning_number:
            cards_found += 1
    
    for i in range(card_id+2, card_id+cards_found+2):
        copy_cards.append(i)

    for copy in copy_cards:
        winning_cards[copy] = winning_cards.get(copy) + winning_cards.get(card_id+1)
 
summ = 0
for key in winning_cards.keys():
    summ+=winning_cards.get(key)
print(summ)