import re

def check_if_impossible(single_value):
    colors = {'blue': 14, 'red': 12, 'green' : 13}
    for val in single_value:
        for color in colors.keys():
            if color in val:
                if (colors.get(color) - int(re.findall('\d+', val)[0])) < 0: 
                    return True
                break
    return False


def main():
    with open('input.txt','r') as f:
        lines = f.read().splitlines()

    games = []
    possible_game = []

    for line in lines:
        games.append(line.split(':')[1].split(';'))

    for game, id in zip(games,range(1,len(games)+1)):
        impossible = False
        for retake in game:
            single_value = retake.split(',')
            impossible = check_if_impossible(single_value)
            if impossible: 
                break
        if not impossible:
            possible_game.append(id)
    print(sum(possible_game))

if __name__ == "__main__":
    main()