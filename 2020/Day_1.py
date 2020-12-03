# Advent of Code 2020 - Day 1

# Read Input File and split at new lines
numbers = open('input_day1.txt').read().split('\n')
year = 2020


def searchFor2020_pt1():
    for i in range(len(numbers)):
        # All values in the list are currently Strings, so we need to cast them to int to be able to calculate with them
        oneint = int(numbers[i])
        for j in range(len(numbers)):
            twoint = int(numbers[j])
            if (oneint + twoint) == year:
                return oneint * twoint

def searchFor2020_pt2():
    # Part two is quite easy, all we need to do is add a third number
    for i in range(len(numbers)):
        oneint = int(numbers[i])
        for j in range(len(numbers)):
            twoint = int(numbers[j])
            for k in range(len(numbers)):
                threeint = int(numbers[k])
                if (oneint + twoint + threeint) == year:
                    return oneint * twoint * threeint


if __name__ == "__main__":
    resultpt1 = searchFor2020_pt1()
    resultpt2 = searchFor2020_pt2()
    print("Welcome to Advent of Code 2020! :-)")
    print("The results are in:")
    print("Part 1: ", resultpt1)
    print("Part 2: ", resultpt2)