import re

# get puzzle input
def get_input():
    return open("./inputs/02.txt")

def part_one():
    puzzle_input = get_input()

    game_id = 1
    valid_ids = 0

    for line in puzzle_input:
        if valid_game(line.rstrip()):
            # print("Game " + str(game_id) + " was valid")
            valid_ids += game_id
        game_id += 1

    print("The sum of the valid game ids is " + str(valid_ids))

def valid_game(line):
    colour_cubes = {"red": 12, "green": 13, "blue": 14}

    for colour, amount in colour_cubes.items():
        for match in re.finditer(colour, line):
            count = int(line[match.start() - 3] + line[match.start() - 2].strip())
            if count > amount:
                return False

    return True

def part_two():
    puzzle_input = get_input()
    sum_of_powers = 0

    for line in puzzle_input:
        sum_of_powers += get_power(line)

    print("Sum of powers " + str(sum_of_powers))

def get_power(line):
    min_cubes = {"red": -1, "green": -1, "blue": -1}

    for colour in min_cubes.keys():
        for match in re.finditer(colour, line):
            count = int(line[match.start() - 3] + line[match.start() - 2].strip())
            min_cubes[colour] = count if count > min_cubes[colour] else min_cubes[colour]

    power = 1
    for value in min_cubes.values():
        power *= value
    
    return power

part_two()

example_input = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
