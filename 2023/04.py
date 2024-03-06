def part1(puzzle_input):
    # 33611 was too high
    points = 0

    for line in puzzle_input:
        winning_numbers, drawn_numbers = format_input(line.rstrip())
        count = winning_no_count(winning_numbers, drawn_numbers)
        points += pow(2, count - 1) if count > 0 else 0

    return points

def format_input(line):
    index = line.find(":") + 1
    split_line = line[index:].split("|")
    return [split_line[0].split(), split_line[1]]

def winning_no_count(winning_numbers, drawn_numbers):
    # problem's likely here
    count = 0
    for number in winning_numbers:
        if number in drawn_numbers: count += 1
    return count

example_input = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

puzzle_input = open("./inputs/04.txt")

print("Cards score: " + str(part1(puzzle_input)))