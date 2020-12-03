input = open('input_day2.txt').read().split('\n')


def checkforletters():
    count = 0
    word = "aaa"
    threeletters = []
    twoletters = []
    countedtwo = 0
    countedthree = 0
    c2temp = 0
    c3temp = 0

    for i in range(len(word)):
        for j in range(len(word) - i):
            if word[i - 1] == word[(i - 1) + j]:
                count += 1

        if count == 2:
            c2temp += 1
            count = 0

        if count == 3:
            c3temp += 1
            count = 0

    if c2temp != 0:
        countedtwo += 1
        c2temp = 0

    if c3temp != 0:
        countedthree += 1
        c3temp = 0

    print(countedtwo, countedthree)


checkforletters()
