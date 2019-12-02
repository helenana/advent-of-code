import math


numbers = [100152, 121802, 140047, 92337, 101891, 122051, 50384, 53628, 139979, 57959, 90354, 119201, 53941, 74563,
           140320, 69972, 90954, 85414, 52999, 69869, 65511, 91084, 146614, 120976, 145517, 121313, 99155, 144062,
           53343, 60992, 81324, 109565, 83665, 100255, 116562, 71967, 66486, 76844, 83233, 129089, 98787, 118848,
           120030, 123908, 144800, 113563, 74763, 80902, 58740, 115929, 57926, 61739, 118481, 111540, 55259, 90161,
           110745, 85103, 92616, 126402, 71906, 137282, 76811, 124470, 140723, 89796, 98126, 127274, 104925, 120395,
           134417, 105281, 140414, 52683, 149260, 123259, 125238, 68860, 103545, 90308, 118854, 121111, 72989, 62993,
           96615, 145935, 75078, 96752, 118779, 68090, 95136, 82132, 149426, 51496, 70123, 129725, 63022, 74422,
           143216, 139349]


def calc_fuel():
    answer = 0
    for index in range(len(numbers)):
        answer += (math.floor(numbers[index] / 3)) - 2
    print(answer)


def calc(number):
    return (math.floor(number / 3)) - 2


def calc_fuel_modules():
    answer = 0

    for index in range(len(numbers)):
        answertemp = 0
        fuel = calc(numbers[index])

        while fuel > 6:
            answertemp += fuel
            fuel = calc(fuel)

        answertemp += fuel
        answer += answertemp

    print("All modules:", answer)


calc_fuel_modules()


def calc_test():
    answer = 0
    module = 122
    fuel = (math.floor(module / 3)) - 2

    if fuel > 6:

        while fuel > 6:
            answer += fuel
            fuel = (math.floor(fuel / 3)) - 2

        else:
            answer += fuel
            print(answer)


calc_test()
