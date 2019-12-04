import csv

# My first try, it did not work out too well... See the new and refactored Version below

path1 = []
path2 = []

with open('input_day3.txt', newline='') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=",")

    for row in csvReader:
        for element in row:
            path1.append(element)

with open('input_day3.txt', newline='') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=",")

    for row in csvReader:
        for element in row:
            path2.append(element)


def calc_steps(path1: list, path2: list):
    # Starting Point is 1/1
    # Horizontal Coordinate
    x1 = []
    x2 = []
    x1temp = 1
    x2temp = 1
    # Vertical Coordinate
    y1 = []
    y2 = []
    y1temp = 1
    y2temp = 1


    for i in range(len(path2)):

        if path2[i][0] == 'U':
            y2temp += int(path2[i][1:])
            y2.append(y2temp)
            x2.append(x2temp)

        if path2[i][0] == 'D':
            y2temp -= int(path2[i][1:])
            y2.append(y2temp)
            x2.append(x2temp)

        if path2[i][0] == 'L':
            x2temp -= int(path2[i][1:])
            x2.append(x2temp)
            y2.append(y2temp)

        if path2[i][0] == 'R':
            x2temp += int(path2[i][1:])
            x2.append(x2temp)
            y2.append(y2temp)

# calc_steps(path1, path2)

# New Version starts from here!


Line1, Line2, _ = open('input_day3.txt').read().split('\n')
Line1, Line2 = [x.split(',') for x in [Line1, Line2]]


def draw_the_line(input):
    x = 0
    y = 0
    length = 0
    answers = {}

    for steps in input:
        d = steps[0]
        n = int(steps[1:])

        for i in range(n):

            if d == "L":
                x -= 1

            if d == "R":
                x += 1

            if d == "U":
                y += 1

            if d == "D":
                y -= 1

            length += 1

            if (x, y) not in answers:
                answers[(x, y)] = length
    return answers


if __name__ == "__main__":

    path1 = draw_the_line(Line1)
    path2 = draw_the_line(Line2)
    combined_paths = set(path1.keys()) & set(path2.keys())

    part1 = min([abs(x) + abs(y) for (x, y) in combined_paths])
    part2 = min([path1[p] + path2[p] for p in combined_paths])

    print("~ My results - Day 3 ~")

    print("Solution for Part 1 - Manhattan Distance: ", part1)

    print("Solution for Part 2 - Total of fewest steps to the next Intersection: ", part2)
