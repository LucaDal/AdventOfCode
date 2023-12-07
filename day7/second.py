cards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']

def sort(winning_lsit):
    final_list = []
    for val in range(7):
        sorting_list = []
        for hand in winning_lsit:
            if hand[1] == val:
                sorting_list.append(hand[0])
        len_new_list = len(sorting_list)
        for index in range(len_new_list-1): 
            flag = False 
            for index_comparing in range(len_new_list-1):

                if index_comparing != index:
                    char_index = 0
                    while cards.index(sorting_list[index_comparing][0][char_index]) == cards.index(sorting_list[index_comparing+1][0][char_index]) and char_index < 4:
                        char_index +=1
                    if cards.index(sorting_list[index_comparing][0][char_index]) > cards.index(sorting_list[index_comparing+1][0][char_index]):
                        sorting_list[index_comparing],sorting_list[index_comparing+1] = sorting_list[index_comparing+1],sorting_list[index_comparing]
                        flag = True
            if not flag:
                break
    return final_list


def highr_card(hand):
    higher_card = 'J'
    for card in cards:
        
        if hand.count(card) > max_freq:
            max_freq = hand.count(card)
            char = card


def get_high_value(hand):

    if 'J' not in hand:
        return hand
    jack = hand.count('J')
    if jack >= 2:

    max_freq = 0
    char = ''
    for card in cards:
        if hand.count(card) > max_freq:
            max_freq = hand.count(card)
            char = card
    print
        

def get_hand_points(hand):
    
    Three_of_a_kind = False
    one_pair = False
    pairs : int = 0
    for card in cards:
        #full
        if hand.count(card) == 5:
            return 6
        #four_of_a_kind
        if hand.count(card) == 4:
            return 5
        if hand.count(card) == 3:
            Three_of_a_kind = True
        if hand.count(card) == 2:
            one_pair = True
            pairs += 1
    if Three_of_a_kind and one_pair: # Full_house failed
        return 4
    elif Three_of_a_kind: # Three of a kind
        return 3 
    if one_pair and pairs == 2:
        return 2
    elif pairs == 1:
        return 1
    return 0

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

winning_list = []
for line in lines:
    values = line.split()
    hand = get_hand_points(hand)
    value_hand = get_hand_points(values[0])
    winning_list.append((values, value_hand))

winning_list.sort(key= lambda x : x[1])
winning_list = sort(winning_list)

print(sum(int(i[1])*index for i,index in zip(winning_list,range(1,len(winning_list)+1))))
