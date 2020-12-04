# Advent of Code 2020 - Day 2

# Read Input from File
with open('input_day2.txt') as file:
    data = [line.replace('-', ' ').replace(':', ' ').strip().split() for line in file]


def checkPwd_1(mini, maxi, letter, password):
    result = 0
    for i in range(len(password)):
        if password[i] == letter:
            result += 1

# If the count of letter is bigger or equal mini or smaller or equal maxi, password is valid
    if int(mini) <= result <= int(maxi):
        return True

    else:
        return False


def checkPwd_2(mini, maxi, letter, password):

    pos1 = int(mini)-1
    pos2 = int(maxi)-1

# Password is valid if char on pos1 OR char on pos2 equals letter

    if password[pos1] == letter and password[pos2] != letter:
        return True

    if password[pos1] != letter and password[pos2] == letter:
        return True

    else:
        return False


if __name__ == "__main__":
    valid_1 = 0
    valid_2 = 0

    for line in data:
        if checkPwd_1(*line):
            valid_1 += 1

    for line in data:
        if checkPwd_2(*line):
            valid_2 += 1

    print('Welcome to Advent of Code Day 2!')
    print('Result for Password Check Pt 1: ', valid_1)
    print('Result for Password Check Pt 2: ', valid_2)
