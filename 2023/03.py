def get_input():
    file = open("./inputs/03.txt")
    text = []
    for line in file:
        text.append(line.rstrip())

    return text

def part_one():
    digits = "0123456789"
    puzzle_input = get_input()

    parts_sum = 0

    for row in range(len(puzzle_input)):
        current_num = ""
        num_positions = []
        for col in range(len(puzzle_input[row])):
            if puzzle_input[row][col] in digits:
                current_num += puzzle_input[row][col]
                num_positions.append([row, col])

                if col == len(puzzle_input) - 1 and current_num:
                    for position in num_positions:
                        if is_adjacent(position, puzzle_input):
                            parts_sum += int(current_num)
                            break
                    break

            elif current_num:
                for position in num_positions:
                    if is_adjacent(position, puzzle_input):
                        parts_sum += int(current_num)
                        break
                current_num = ""
                num_positions = []

    print("Part number sum: " + str(parts_sum))

def is_adjacent(centre, puzzle_input):
    excluded = ".0123456789"
    positions = [[-1,-1], [-1, 0], [-1, 1], [ 0,-1], [ 0, 1], [ 1,-1], [ 1, 0], [ 1, 1]]

    for position in positions:
        row = centre[0] + position[0]
        col = centre[1] + position[1]

        if row < 0 or col < 0 or row >= len(puzzle_input[0]) or col >= len(puzzle_input):
            continue

        if puzzle_input[row][col] not in excluded:
            return True

    return False

def get_possible_gears(centre, puzzle_input):
    positions = [[-1,-1], [-1, 0], [-1, 1], [ 0,-1], [ 0, 1], [ 1,-1], [ 1, 0], [ 1, 1]]

    possible_gear_positions = []    

    for position in positions:
        row = centre[0] + position[0]
        col = centre[1] + position[1]

        if row < 0 or col < 0 or row >= len(puzzle_input[0]) or col >= len(puzzle_input):
            continue

        if puzzle_input[row][col] == "*":
            possible_gear_positions.append([row, col])

    return possible_gear_positions

def part_two():
    digits = "0123456789"
    puzzle_input = get_input()

    possible_gears = {}
    gear_ratio_sum = 0

    for row in range(len(puzzle_input)):
        current_num = ""
        num_positions = []
        for col in range(len(puzzle_input[row])):
            if puzzle_input[row][col] in digits:
                current_num += puzzle_input[row][col]
                num_positions.append([row, col])

                if col == len(puzzle_input) - 1 and current_num:
                    for position in num_positions:
                        symbol_positions = get_possible_gears(position,puzzle_input)
                        if symbol_positions:
                            for symbol_pos in symbol_positions:
                                key = str(symbol_pos[0]) + "," + str(symbol_pos[1])
                                possible_gears.setdefault(key, []).append(current_num)
                            break
                    break

            elif current_num:
                for position in num_positions:
                    symbol_positions = get_possible_gears(position,puzzle_input)
                    if symbol_positions:
                        for symbol_pos in symbol_positions:
                            key = str(symbol_pos[0]) + "," + str(symbol_pos[1])
                            possible_gears.setdefault(key, []).append(current_num)
                        break
                current_num = ""
                num_positions = []

    print(possible_gears)
    for value in possible_gears.values():
        if len(value) == 2:
            gear_ratio_sum += int(value[0]) * int(value[1])

    print("Gear ratio sum: " + str(gear_ratio_sum))

part_two()

example_input = ["467..114..", 
                 "...*......",
                 "..35..633.",
                 "......#...",
                 "617*......",
                 ".....+.58.",
                 "..592.....",
                 "......755.",
                 "...$.*....",
                 ".664.598.."]
