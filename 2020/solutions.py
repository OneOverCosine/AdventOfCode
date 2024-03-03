import re


def readInput(filename, as_int=False, delim=""):
    file = open(filename + ".txt")
    file_output = []

    if (as_int):
        for line in file.readlines():
            file_output.append(int(line.rstrip()))
    elif (delim != ""):
        entry = ""
        for line in file.readlines():
            if (line == delim):
                file_output.append(entry)
                entry = ""
            else:
                entry += " " + line.rstrip()
    else:
        for line in file.readlines():
            file_output.append(line.rstrip())

    return file_output


def day1(part):

    comparisons = 0
    expense_report = readInput("01", True)
    target = 2020

    if (part == 1):
        # 10901 comparisons
        # for item1 in expense_report:
        #     for item2 in expense_report:
        #         comparisons += 1
        #         if (item1 + item2 == target):
        #             print("answer found in " +
        #                   str(comparisons) + " comparisions")
        #             return item1 * item2

        # 9361 comparisons
        for i in range(len(expense_report)):
            for j in range(i+1, len(expense_report)):
                comparisons += 1
                if (expense_report[i] + expense_report[j] == target):
                    print("answer found in " +
                          str(comparisons) + " comparisions")
                    return expense_report[i] * expense_report[j]
    else:
        # 499970 comparisons
        # for item1 in expense_report:
        #     for item2 in expense_report:
        #         for item3 in expense_report:
        #             comparisons += 1
        #             if (item1 + item2 + item3 == target):
        #                 print("answer found in " +
        #                       str(comparisons) + " comparisions")
        #                 return item1 * item2 * item3

        # 235975 comparisons
        for i in range(len(expense_report)):
            for j in range(i+1, len(expense_report)):
                for k in range(j+1, len(expense_report)):
                    comparisons += 1
                    if (expense_report[i] + expense_report[j] + expense_report[k] == target):
                        print("answer found in " +
                              str(comparisons) + " comparisions")
                        return expense_report[i] * expense_report[j] * expense_report[k]
    return 0


def day2(part):
    pass_policies = readInput("02")
    valid = 0

    # for pass_policy in pass_policies:
    #     pass_policy = pass_policy.split(": ")
    #     password = pass_policy[1]
    #     policy = day2_split_policy(pass_policy[0])

    #     if (password.count(policy[2]) >= policy[0] and password.count(policy[2]) <= policy[1]):
    #         valid += 1

    if (part == 1):
        for pass_policy in pass_policies:
            pol_min, pol_max, pol_char, password = day2_split_pass_policy(
                pass_policy)

            if (password.count(pol_char) >= pol_min and password.count(pol_char) <= pol_max):
                valid += 1
    else:
        for pass_policy in pass_policies:
            first, last, pol_char, password = day2_split_pass_policy(
                pass_policy)

            if(password[first-1] == pol_char and password[last-1] != pol_char):
                valid += 1
            elif(password[first-1] != pol_char and password[last-1] == pol_char):
                valid += 1

    return valid


def day2_split_pass_policy(pass_policy):
    pass_policy = re.findall(r"[\w\d]+", pass_policy)
    return int(pass_policy[0]), int(pass_policy[1]), pass_policy[2], pass_policy[3]


def day3(part):
    grid = readInput("03")
    repeat_length = len(grid[0])
    result = 0

    if (part == 1):
        result = day3_get_tree_count(grid, 3, 1, repeat_length)

    else:
        result = 145  # answer from previous part of the puzzle
        slopes = [[1, 1], [5, 1], [7, 1], [1, 2]]
        for slope in slopes:
            tree_count = day3_get_tree_count(
                grid, slope[0], slope[1], repeat_length)
            result = result * tree_count

    print("Result: " + str(result))


def day3_get_tree_count(grid, left_step, down_step, repeat_length):
    pos_left = 0
    pos_down = 0
    tree_count = 0
    while (pos_down + 1 < len(grid)):
        pos_left = (pos_left + left_step) % repeat_length
        pos_down += down_step
        tree_count = tree_count + \
            1 if grid[pos_down][pos_left] == "#" else tree_count
    return tree_count


def day4(part):
    passports = readInput("04", delim="\n")
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional = "cid"

    for passport in passports:
        fields = passport.split()
        # fields = re.split("\:", passport)  # [0::2]
        print("Passport: " + passport + "\n-----")
        print("Fields: " + str(fields) + "\n---------------")


# print("Result: " + str(day1(2)))
# print("Valid passwords: " + str(day2(2)))
# day3(2)
day4(1)
