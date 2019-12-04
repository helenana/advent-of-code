input = open('input_day1.txt').read().split('\n')

# This might be the slowest Code ever... But it works! Finds Frequency that was reached twice in Loop 137


def calc_frequency():

    myinput = input[:]
    answer = 0
    answerlist = [0]
    inlength = len(myinput)
    reset = 0
    i = 0

    while i < inlength:

        operator = myinput[i][0]
        number = int(myinput[i][1:])

        if operator == "+":
            answer += number
            i += 1

        else:
            answer -= number
            i += 1

        if answer not in answerlist:

            if i == inlength - 1:
                i = 0
                reset += 1
                print("reset No. ", reset)

            answerlist.append(answer)

        else:
            print("Frequency ", answer, " was reached Twice")
            break

    return answer


print(calc_frequency())
