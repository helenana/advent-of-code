input_picture = open('input_day8.txt').read()


def space_image_calc(wide, tall):

    length = (wide * tall)
    layers = []
    numlayers = int(len(input_picture) / length)

    countstart = 0
    countend = length

    countzero = length
    countzerotemp = 0
    countone= 0
    counttwo = 0

    for i in range(100):
        layers.append(input_picture[countstart:countend])
        countstart += length
        countend += length

    print(layers)

    for i in range(100):

        for j in range(150):

            if int(layers[i][j]) == 0:
                countzerotemp += 1

            elif int(layers[i][j]) == 1:
                countone += 1

            elif int(layers[i][j]) == 2:
                counttwo += 1

        if countzerotemp < countzero:
            countzero = countzerotemp
            result = countone * counttwo
            print(countone + counttwo + countzero)
            print(result)

        countzerotemp = 0
        countone = 0
        counttwo = 0

#        print(countzero)


space_image_calc(25, 6)
