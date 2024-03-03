# get puzzle input
def get_input():
    return open("./inputs/01.txt")


def first_and_last(line):
    digits = "123456789"  # the input file doesn't contain any 0's
    value = ""

    for character in line:
        if character in digits:
            value = character
            break

    for character in line[::-1]:
        if character in digits:
            value += character
            break

    return int(value)


def convert_to_digits(line):
    numbers = {"one": "1", "two": "2", "three": "3", "four": "4",
               "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    temp_line = ""

    for i in range(len(line)):
        if line[i] in numbers.values():
            temp_line += line[i]
            continue
        for number in numbers.keys():
            current = line[i:i+len(number)]
            if current == number:
                temp_line += numbers[number]
                break
            # temp_line += line[i]

    return temp_line


def day01_part1():
    puzzle_input = get_input()
    calibration_sum = 0

    for line in puzzle_input:
        calibration_sum += first_and_last(line.rstrip())

    print("Calibration sum: " + str(calibration_sum))


def day01_part2():
    puzzle_input = get_input()
    calibration_sum = 0

    for line in puzzle_input:
        value = replace_strings(line)
        value = value[0] + value[-1]
        calibration_sum += int(value)

    print("Calibration sum: " + str(calibration_sum))


day01_part1()
day01_part2()

example_input = ["two1nine", 
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"]
