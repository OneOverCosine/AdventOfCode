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

def gear_ratio(row, col, puzzle_input):
    positions = [[-1,-1], [-1, 0], [-1, 1], [ 0,-1], [ 0, 1], [ 1,-1], [ 1, 0], [ 1, 1]]
    
    

def part_two():
    puzzle_input = ["467..114..", 
                    "...*......",
                    "..35..633.",
                    "......#...",
                    "617*......",
                    ".....+.58.",
                    "..592.....",
                    "......755.",
                    "...$.*....",
                    ".664.598.."]

    for row in range(len(puzzle_input)):
        if "*" not in puzzle_input[row]: continue
        for col in range(len(puzzle_input[row])):
            if puzzle_input[row][col] == "*":
                print(row, col)

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
