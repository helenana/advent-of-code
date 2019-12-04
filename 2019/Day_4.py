
def check_password(password, part) -> bool:

    password = str(password)

    def check_increasing(password: str) -> bool:

        pwlist = list(password)
        increasing = True

        for i, x in enumerate(pwlist):
            if i > 0:
                if int(pwlist[i - 1]) > int(x):

                    increasing = False
                    break

        if increasing:
            return True

        else:
            return False

    def check_samedigits(password: str) -> bool:

        pwlist = list(password)

        if (pwlist[0] == pwlist[1]) | (pwlist[1] == pwlist[2]) | (pwlist[2] == pwlist[3]) | (pwlist[3] == pwlist[4]) | \
                (pwlist[4] == pwlist[5]):
            return True

        else:
            return False

    # For part two we need to check if a number appears more than twice -> if a number appears more than twice in
    # a sequence "check_morethantwice" will return false

    def check_morethantwice(password: str) -> bool:

        pwlist = list(password)

        if (pwlist[0] == pwlist[1]) & (pwlist[2] != pwlist[1]) | \
                (pwlist[1] == pwlist[2]) & (pwlist[3] != pwlist[2]) & (pwlist[1] != pwlist[0]) | \
                (pwlist[2] == pwlist[3]) & (pwlist[4] != pwlist[3]) & (pwlist[2] != pwlist[1]) | \
                (pwlist[3] == pwlist[4]) & (pwlist[5] != pwlist[4]) & (pwlist[3] != pwlist[2]) | \
                (pwlist[4] == pwlist[5]) & (pwlist[4] != pwlist[3]):
            return True

        else: return False

    # For part one:
    if part == 1:

        if (check_increasing(password) == True) & (check_samedigits(password) == True):
            return True

        else:
            return False

    # For part two:
    if part == 2:

        if (check_increasing(password) == True) & (check_morethantwice(password) == True):
            return True

        else:
            return False


if __name__ == "__main__":

    validpwspt1 = 0
    validpwspt2 = 0
    myrange = range(165432, 707912)

    for i in myrange:

        if check_password(i, 1):
            validpwspt1 += 1

        if check_password(i, 2):
            validpwspt2 += 1

    print("~ My results - Day 4 ~")
    print("Results for Part 1: ", validpwspt1)
    print("Results for Part 2: ", validpwspt2)
