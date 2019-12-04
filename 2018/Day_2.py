input = open('input_day2.txt').read().split('\n')

def checkforletters():

    count = 0
    word = "aabtkuy"
    threeletters = []
    twoletters = []
    countedtwo = 0
    countedthree = 0

    for i in range(len(word)):
        for j in range(len(word)):
            if word[i] == word[j]:
                count += 1

        if count == 2:


        print(count)


checkforletters()