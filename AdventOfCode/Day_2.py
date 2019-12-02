truenumbers = [1, 12, 2, 3,
           1, 1, 2, 3,
           1, 3, 4, 3,
           1, 5, 0, 3,
           2, 1, 13, 19,
           1, 9, 19, 23,
           1, 6, 23, 27,
           2, 27, 9, 31,
           2, 6, 31, 35,
           1, 5, 35, 39,
           1, 10, 39, 43,
           1, 43, 13, 47,
           1, 47, 9, 51,
           1, 51, 9, 55,
           1, 55, 9, 59,
           2, 9, 59, 63,
           2, 9, 63, 67,
           1, 5, 67, 71,
           2, 13, 71, 75,
           1, 6, 75, 79,
           1, 10, 79, 83,
           2, 6, 83, 87,
           1, 87, 5, 91,
           1, 91, 9, 95,
           1, 95, 10, 99,
           2, 9, 99, 103,
           1, 5, 103, 107,
           1, 5, 107, 111,
           2, 111, 10, 115,
           1, 6, 115, 119,
           2, 10, 119, 123,
           1, 6, 123, 127,
           1, 127, 5, 131,
           2, 9, 131, 135,
           1, 5, 135, 139,
           1, 139, 10, 143,
           1, 143, 2, 147,
           1, 147, 5, 0,
           99, 2, 0, 14,
           0]

# Day 2 - Part 1
# Just a small test to see if I can print the numbers correctly


def print_numbers():

    count = 0

    while count < len(truenumbers):
        print(truenumbers[count])
        count += 4


def intcode(noun: int, verb: int) -> int:

    # Copy truenumbers Array to new Array

    numbers = truenumbers[:]

    count = 0
    numbers[1] = noun
    numbers[2] = verb

    while count < len(numbers):

        if numbers[count] == 1:
            pos1 = numbers[count+1]
            pos2 = numbers[count+2]
            pos3 = numbers[count+3]

            numbers[pos3] = numbers[pos1] + numbers[pos2]

            count += 4

        elif numbers[count] == 2:
            pos1 = numbers[count+1]
            pos2 = numbers[count+2]
            pos3 = numbers[count+3]

            numbers[pos3] = numbers[pos1] * numbers[pos2]

            count += 4

        else:
            return numbers[0]


# Day 2 - Part 2

def print_loop():

    for i in range(100):
        for j in range(100):
            print(i, j)


def find_result(target: int):

    for i in range(100):

        for j in range(100):
            result = intcode(i, j)

            if target == result:
                return i * 100 + j


if __name__ == "__main__":

    print("~ My results ~")

    # Result for Part 1:

    print("Result for Part 1: ", intcode(12, 2))

    # Result for Part 2:

    print("Result for Part 2: ", find_result(19690720))
