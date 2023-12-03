
import re

def check_min_cubes(single_value, min):
    colors = {'blue','red', 'green'}
    for val in single_value:
        for color in colors:
            if color in val:
                if min.get(color) < int(re.findall('\d+', val)[0]):
                    min[color] = int(re.findall('\d+', val)[0])
                break


def main():
    with open('input.txt','r') as f:
        lines = f.read().splitlines()

    games = []
    possible_game = []

    for line in lines:
        games.append(line.split(':')[1].split(';'))

    for game in games:
        min = {'blue': 0, 'red': 0, 'green' : 0}
        cube_power = 1
        for retake in game:
            single_value = retake.split(',')
            check_min_cubes(single_value, min)
        for val in min.keys():
            cube_power *= min.get(val)
        possible_game.append(cube_power)
    print(sum(possible_game))

if __name__ == "__main__":
    main()