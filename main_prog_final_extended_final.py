#------------------------------------
#       Importing libraries
#------------------------------------

import random
import os
import sys
import time
import readchar


#------------------------------------
#        Creating the matrix
#------------------------------------
gamebox = list()
gamestate = 'not over'
validmove = True
score = 0


def init():
    global gamebox
    global score
    score = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    gamebox = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
    gamebox_random()


def easy_win():
    global gamebox
    global score
    score = 'Its Over 9000!!!'
    gamebox = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 2048]]


def easy_lose():
    global gamebox
    global score
    score = '-0'
    gamebox = [[16, 8, 4, 2],
               [8, 16, 8, 4],
               [4, 8, 16, 8],
               [2, 4, 8, 0]]

#------------------------------------
#        Graphics print
#------------------------------------


def logo_print():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("     `..--..`        ``.--..`             `...`      `..---.`         ")
    print("   ./oooooooo/.    `:+ooooooo/.         `-+ooo:    `/oooooooo+:`      ")
    print("  `-/o+-..:ooo+`  `+ooo:..-+ooo-       ./ooooo:   `/oo+-``.:ooo-      ")
    print("     `    `+ooo`  -ooo:    `+oo+`    `:ooo/ooo:   `/oo+-` `:ooo-      ")
    print("         `/ooo:   /ooo.     /ooo.   .+oo+.`+oo:    `-+ooo+ooo:.       ")
    print("       `:ooo+.    /ooo.     /ooo. `:ooo-` `+oo:    ./ooo//+oo+:`      ")
    print("     ./ooo/-`     :ooo-    `+oo+``/ooo/::::ooo/:- .ooo/`   .+oo/      ")
    print("  `-/ooo+-.....`  `+oo+-```/ooo: `+ooooooooooooo/ .ooo/`   .+oo+`     ")
    print("  `+ooooooooooo/   .+oooo+oooo:`  ````````.+oo:`` `:oooo+++ooo+.      ")
    print("  `------------.     .-://::-`            `---.     `.-:::::-.        ")
    print("\n" * 2)
    print("                   Press any Enter to start")


def win_print():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("                    `s:   .y.`+ssss+`  s:    s/                       ")
    print("                     `hs /d-`mo    om` mo    mo                       ")
    print("                       oNy` +m      N/ mo    mo                       ")
    print("                       `M:  -M.    -M- do    m+                       ")
    print("                       `M:   :hs++sh:  :ds++yh`                       ")
    print("                        `      `..`      `..                          ")
    print("                     .`   `.    .    .--`    ..    .`                 ")
    print("                     yy  `mm.  od  od+:/sd-  NNo   M:                 ")
    print("                     .M. os+y `N: om     /N` N+hs  M:                 ")
    print("                      yy`N` m.od  yh     .M. N/ ys`M:                 ")
    print("                      .Mys  +hN:  .N+   .hy  N/  yyM:                 ")
    print("                       +s`   so    `+ssso-   s-   +s.                 ")
    print("\n" * 2)


def lose_print():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("                    `s:   .y.`+ssss+`  s:    s/                       ")
    print("                     `hs /d-`mo    om` mo    mo                       ")
    print("                       oNy` +N      N/ mo    mo                       ")
    print("                       `M:  -M.    -M- do    m+                       ")
    print("                       `M:   :hs++sh:  :ds++yh`                       ")
    print("                        `      `..`      `..                          ")
    print("                      .        .--`     .--.`  `.....                 ")
    print("                     -M`    `sh+:/yh. .mo/:/+  hh++++`                ")
    print("                     -M`    sh     +m -N+-.    hy----                 ")
    print("                     -M`    hs     :M` `:+ohh` hh::::                 ")
    print("                     -M`    :N/   .do ``   .M: hs                     ")
    print("                     .sssss+ `+ssso-  .ossss:  +sssss-                ")
    print("\n" * 2)

#------------------------------------
#        Drawing the matrix
#------------------------------------


def gamebox_draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Score: ", score)
    print("\n")
    for i in range(0, 4):
        for j in range(0, 4):
            if j == 3:
                print('\33[33m', '{:4d}'.format(gamebox[i][j]), '\x1b[0m', end="\n" * 2)
            else:
                print('\33[33m', '{:4d}'.format(gamebox[i][j]), '\x1b[0m', end=" ")
    print("\n")


#------------------------------------
#  Ordering the items of the matrix
#------------------------------------
def gamebox_order_left():
    a = 0
    movement_happened = False
    while (a != 4):
        for i in range(0, 3):
            for j in range(0, 3):
                if gamebox[a][j] == 0 and gamebox[a][j + 1] != 0:
                    gamebox[a][j] = gamebox[a][j + 1]
                    gamebox[a][j + 1] = 0
                    movement_happened = True
        a += 1
    return movement_happened


def gamebox_order_right():
    a = 0
    movement_happened = False
    while (a != 4):
        for i in range(0, 3):
            for j in reversed(range(1, 4)):
                if gamebox[a][j] == 0 and gamebox[a][j - 1] != 0:
                    gamebox[a][j] = gamebox[a][j - 1]
                    gamebox[a][j - 1] = 0
                    movement_happened = True
        a += 1
    return movement_happened


def gamebox_order_up():
    a = 0
    movement_happened = False
    while (a != 4):
        for j in range(0, 3):
            for i in (range(0, 3)):
                if gamebox[i][a] == 0 and gamebox[i + 1][a] != 0:
                    gamebox[i][a] = gamebox[i + 1][a]
                    gamebox[i + 1][a] = 0
                    movement_happened = True
        a += 1
    return movement_happened


def gamebox_order_down():
    a = 0
    movement_happened = False
    while (a != 4):
        for j in range(0, 3):
            for i in reversed(range(1, 4)):
                if gamebox[i][a] == 0 and gamebox[i - 1][a] != 0:
                    gamebox[i][a] = gamebox[i - 1][a]
                    gamebox[i - 1][a] = 0
                    movement_happened = True
        a += 1
    return movement_happened


#------------------------------------
#    Merging the items of the matrix
#------------------------------------
def gamebox_merge_left():
    global score
    a = 0
    movement_happened = False
    while (a != 4):
        for j in range(0, 3):
            if gamebox[a][j] == gamebox[a][j + 1] and gamebox[a][j] != 0:
                gamebox[a][j] *= 2
                score = score + gamebox[a][j]
                gamebox[a][j + 1] = 0
                movement_happened = True
        a += 1
    return movement_happened


def gamebox_merge_right():
    global score
    a = 0
    movement_happened = False
    while (a != 4):
        for j in reversed(range(1, 4)):
            if gamebox[a][j] == gamebox[a][j - 1] and gamebox[a][j] != 0:
                gamebox[a][j] *= 2
                score = score + gamebox[a][j]
                gamebox[a][j - 1] = 0
                movement_happened = True
        a += 1
    return movement_happened


def gamebox_merge_up():
    global score
    a = 0
    movement_happened = False
    while (a != 4):
        for i in (range(0, 3)):
            if gamebox[i][a] == gamebox[i + 1][a] and gamebox[i][a] != 0:
                gamebox[i][a] *= 2
                score = score + gamebox[i][a]
                gamebox[i + 1][a] = 0
                movement_happened = True
        a += 1
    return movement_happened


def gamebox_merge_down():
    global score
    a = 0
    movement_happened = False
    while (a != 4):
        for i in reversed(range(1, 4)):
            if gamebox[i][a] == gamebox[i - 1][a] and gamebox[i][a] != 0:
                gamebox[i][a] *= 2
                score = score + gamebox[i][a]
                gamebox[i - 1][a] = 0
                movement_happened = True
        a += 1
    return movement_happened


def gamebox_order_down():
    a = 0
    movement_happened = False
    while (a != 4):
        for j in range(0, 3):
            for i in reversed(range(1, 4)):
                if gamebox[i][a] == 0 and gamebox[i - 1][a] != 0:
                    gamebox[i][a] = gamebox[i - 1][a]
                    gamebox[i - 1][a] = 0
                    movement_happened = True
        a += 1
    return movement_happened

#------------------------------------
#  Creating the random number in the matrix
#------------------------------------


def gamebox_random():
    while (True):
        rnum1 = random.randrange(0, 4)
        rnum2 = random.randrange(0, 4)
        rlist = (2, 2, 2, 4)
        if gamebox[rnum1][rnum2] == 0:
            gamebox[rnum1][rnum2] = random.choice(rlist)
            break

#------------------------------------
#      Game states
#------------------------------------


def game_validate():
    global gamestate
    gamestate = 'over'
    game_win()
    while (gamestate != 'not over'):
        gamebox_check_left()
        gamebox_check_right()
        gamebox_check_down()
        gamebox_check_up()
        if gamestate == 'over':
            print("you have lost the game!")
            time.sleep(2)
            lose_print()
            sys.exit()


def game_win():
    a = 0
    while (a != 4):
        b = 0
        while (b != 4):
            if gamebox[a][b] == 2048:
                print ("you have won")
                time.sleep(2)
                win_print()
                sys.exit()
            b += 1
        a += 1


def gamebox_check_left():
    global gamestate
    a = 0
    while (a != 4):
        for j in range(0, 3):
            if gamebox[a][j] == gamebox[a][j + 1] or gamebox[a][j] == 0:
                gamestate = 'not over'
                return gamestate
        a += 1


def gamebox_check_right():
    global gamestate
    a = 0
    while (a != 4):
        for j in reversed(range(1, 4)):
            if gamebox[a][j] == gamebox[a][j - 1] or gamebox[a][j] == 0:
                gamestate = 'not over'
                return gamestate
        a += 1


def gamebox_check_down():
    global gamestate
    a = 0
    while (a != 4):
        for i in reversed(range(1, 4)):
            if gamebox[i][a] == gamebox[i - 1][a] or gamebox[i][a] == 0:
                gamestate = 'not over'
                return gamestate
        a += 1


def gamebox_check_up():
    global gamestate
    a = 0
    while (a != 4):
        for i in (range(0, 3)):
            if gamebox[i][a] == gamebox[i + 1][a] or gamebox[i][a] == 0:
                gamestate = 'not over'
                return gamestate
        a += 1


#------------------------------------
#       Matrix actions
#------------------------------------
def gamebox_action_up():
    global validmove
    validmove = False
    if gamebox_order_up() == True:
        validmove = True
    if gamebox_merge_up() == True:
        validmove = True
    if gamebox_order_up() == True:
        validmove = True


def gamebox_action_left():
    global validmove
    validmove = False
    if gamebox_order_left() == True:
        validmove = True
    if gamebox_merge_left() == True:
        validmove = True
    if gamebox_order_left() == True:
        validmove = True


def gamebox_action_down():
    global validmove
    validmove = False
    if gamebox_order_down() == True:
        validmove = True
    if gamebox_merge_down() == True:
        validmove = True
    if gamebox_order_down() == True:
        validmove = True


def gamebox_action_right():
    global validmove
    validmove = False
    if gamebox_order_right() == True:
        validmove = True
    if gamebox_merge_right() == True:
        validmove = True
    if gamebox_order_right() == True:
        validmove = True


#-----------------------------------------------------------

#------------------------------------
#        Main program
#------------------------------------
logo_print()
input()
init()
userinput = None
while (userinput != "quit"):
    if validmove == True:
        gamebox_random()
    gamebox_draw()
    game_validate()
    print("Use the arrow keys to move the blocks and the letter O for additional options")
    while (True):
        userinput = readchar.readkey()
        if userinput == '\x1b[A':
            gamebox_action_up()
            break
        elif userinput == '\x1b[D':
            gamebox_action_left()
            break
        elif userinput == '\x1b[B':
            gamebox_action_down()
            break
        elif userinput == '\x1b[C':
            gamebox_action_right()
            break
        elif userinput == 'o':
            userinput = input("Enter the following options: new game, continue, win, lose, quit: ")
            userinput.lower()
            if userinput == 'new game':
                init()
                break
            elif userinput == 'continue':
                break
            elif userinput == 'win':
                easy_win()
                break
            elif userinput == 'lose':
                easy_lose()
                break
            elif userinput == 'quit':
                sys.exit()
            else:
                print(userinput, "is not a valid option. Please enter: new game, continue, win, lose or quit: ")
                continue
        else:
            gamebox_draw()
            print(userinput, "are not valid character(s)")
            print("Use the arrow keys to move the blocks and the letter O for additional options")
            continue
