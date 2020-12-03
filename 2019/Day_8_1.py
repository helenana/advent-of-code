input_picture = open('input_day8.txt').read()


def space_image_calc(wide, tall):

    length = (wide * tall)
    layers = []


    countstart = 0
    countend = length

    for i in range(100):
        layers.append(input_picture[countstart:countend])
        countstart += length
        countend += length

#    print(layers)

    final_layer = list(layers[0])

    for i in range(100):
        for j in range(150):
            if int(final_layer[j]) == 2:
                final_layer[j] = layers[i][j]

    for i in range(length):
        if int(final_layer[i]) == 1:
            final_layer[i] = "*"

        else:
            final_layer[i] = " "

    print("".join(final_layer))



space_image_calc(25, 6)
