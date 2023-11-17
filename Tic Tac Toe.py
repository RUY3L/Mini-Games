# Tic tac toe

# Takes user input in digits:  1-9

# Checks input against preexisting board

# If empty then places a Q and sets a new X at random

# Otherwise asks to "Use a different number"

# If there is a set of 3 connected Q or X then declares win or lose condition

# If neither than continues to the end

# Finishes the game and resets

from random import seed
from random import randint
seed(1)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6
num7 = 7
num8 = 8
num9 = 9
xvalue = 2

place = [num1, num2, num3, num4, num5, num6, num7, num8, num9]


class Error(Exception):
    pass


class ValueUsed(Error):
    pass

def display_result():
    print()
    print(place[0:3])
    print(place[3:6])
    print(place[6:9])
    print()

def main():
    f = True
    try:
        qValue = int(input("Enter a number  to place a Q: "))
        print()
        indices = [i for i, x in enumerate(place) if x == 'Q']
        indices2 = [i for i, x in enumerate(place) if x == 'X']
        for num in place:
            if num == qValue:
                place[num - 1] = "Q"
                while f == True:
                    xvalue = randint(1, 10)
                    for dum in place:
                        if dum == xvalue:
                            place[dum - 1] = "X"
                            f = False
            elif num != qValue:
                if qValue-1 in indices:
                    # print("Got'em")
                    raise ValueUsed
                elif qValue-1 in indices2:
                    # print("Got'em too")
                    raise ValueUsed
            #
            #     elif num == 'X':
            #         if int(place.index('X', num)) == qValue-1:
            #             print('Mistake')
            #             raise ValueUsed

        # print(place[0:3])
        # print(place[3:6])
        # print(place[6:9])

    except ValueUsed:
        print("Try again, use a number from 1-9 that has not yet been used")
        display_result()
        main()

    except:
        print("Try again, use a number from 1-9 to place a Q in the grid")
        display_result()
        main()

def check():
    if place[0:3] == ['Q', 'Q', 'Q']:
        return True
    elif place[3:6] == ['Q', 'Q', 'Q']:
        return True
    elif place[6:9] == ['Q', 'Q', 'Q']:
        return True
    elif place[0] == 'Q' and place[3] == 'Q' and place[6] == 'Q':
        return True
    elif place[1] == 'Q' and place[4] == 'Q' and place[7] == 'Q':
        return True
    elif place[2] == 'Q' and place[5] == 'Q' and place[8] == 'Q':
        return True
    elif place[0] == 'Q' and place[4] == 'Q' and place[8] == 'Q':
        return True
    elif place[2] == 'Q' and place[4] == 'Q' and place[6] == 'Q':
        return True


def check2():
    
    if place[0:3] == ['X', 'X', 'X']:
        return True
    elif place[3:6] == ['X', 'X', 'X']:
        return True
    elif place[6:9] == ['X', 'X', 'X']:
        return True
    elif place[0] == 'X' and place[3] == 'X' and place[6] == 'X':
        return True
    elif place[1] == 'X' and place[4] == 'X' and place[7] == 'X':
        return True
    elif place[2] == 'X' and place[5] == 'X' and place[8] == 'X':
        return True
    elif place[0] == 'X' and place[4] == 'X' and place[8] == 'X':
        return True
    elif place[2] == 'X' and place[4] == 'X' and place[6] == 'X':
        return True


while True:
    i = 0
    while i < 4:
        i += 1
        display_result()
        main()
        check()
        check2()
        if check() is True:
            i = 9
            display_result()
            print("! (^ O ^)    You win    (^ O ^) !")
            print()

        elif check2() is True:
            display_result()
            print("~  (-_-)    You lose    (-_-)  ~)")
            i = 9
            print()

    else:
        print("\Q/X\Q/X\Q/X\ Game Over /X\Q/X\Q/X\Q/")
        print()
        place = [num1, num2, num3, num4, num5, num6, num7, num8, num9]
        if input("Repeat the program? (Y/N): ").strip().upper() != 'Y':
            print("Done")
            break
