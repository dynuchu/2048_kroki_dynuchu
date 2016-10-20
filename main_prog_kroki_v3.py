import random
import os
import sys

gamebox = list()
def init():
    global gamebox
    gamebox = [[0,0,0,0],
            [0,0,0,0],      
            [0,0,0,0],           
            [0,0,0,0]]
    gamebox_random()
    gamebox_random()

def gamebox_draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0,4):
        for j in range(0,4):
            if j == 3:
                print(gamebox[i][j], end="\n")
            else:
                print(gamebox[i][j], end=" ")
    print("\n")

def gamebox_action():
    gamebox_order()
    gamebox_merge()
    gamebox_order()

def gamebox_validate():
    return True

def gamebox_order_left():
    a = 0
    while (a != 4):
        for i in range(0,3):
            for j in range(0,3):
                if gamebox[a][j] == 0 and gamebox[a][j+1] !=0:
                    gamebox[a][j] = gamebox[a][j+1]
                    gamebox[a][j+1] = 0
        a += 1

def gamebox_order_right():
    a = 0
    while (a != 4):
        for i in range(0,3):
            for j in reversed(range(1,4)):
                if gamebox[a][j] == 0 and gamebox[a][j-1] !=0:
                    gamebox[a][j] = gamebox[a][j-1]
                    gamebox[a][j-1] = 0
        a += 1

def gamebox_order_up():
    a = 0
    while (a !=4):
        for j in range(0,3):
                for i in (range(0,3)):
                    if gamebox[i][a] == 0 and gamebox[i+1][a] !=0:
                        gamebox[i][a] = gamebox[i+1][a]
                        gamebox[i+1][a] = 0
        a += 1

def gamebox_order_down():
    a = 0
    while (a !=4):
        for j in range(0,3):
                for i in reversed(range(1,4)):
                    if gamebox[i][a] == 0 and gamebox[i-1][a] !=0:
                        gamebox[i][a] = gamebox[i-1][a]
                        gamebox[i-1][a] = 0
        a += 1

def gamebox_merge_left():
    a = 0
    while (a != 4):
        for i in range(0,3):
            for j in range(0,3):
                if gamebox[a][j] == gamebox[a][j+1] and gamebox[a][j] !=0:
                    gamebox[a][j] *= 2
                    gamebox[a][j+1] = 0
        a += 1                

def gamebox_merge_right():
    a = 0
    while (a != 4):
        for i in range(0,3):
            for j in reversed(range(1,4)):
                if gamebox[a][j] == gamebox[a][j-1] and gamebox[a][j] !=0:
                    gamebox[a][j] *= 2
                    gamebox[a][j-1] = 0
        a += 1   

def gamebox_merge_up():
    a = 0
    while (a !=4):
        for j in range(0,3):
                for i in (range(0,3)):
                    if gamebox[i][a] == gamebox[i+1][a] and gamebox[i][a]!=0: 
                        gamebox[i][a] *= 2
                        gamebox[i+1][a] = 0
        a += 1


def gamebox_merge_down():
    a = 0
    while (a !=4):
        for j in range(0,3):
                for i in reversed(range(1,4)):
                    if gamebox[i][a] == gamebox[i-1][a] and gamebox[i][a] !=0:
                        gamebox[i][a] *= 2
                        gamebox[i-1][a] = 0
        a += 1

def gamebox_order_down():
    a = 0
    while (a !=4):
        for j in range(0,3):
                for i in reversed(range(1,4)):
                    if gamebox[i][a] == 0 and gamebox[i-1][a] !=0:
                        gamebox[i][a] = gamebox[i-1][a]
                        gamebox[i-1][a] = 0
        a += 1

def gamebox_random():
    while (True):
        rnum1 = random.randrange(0,4)
        rnum2 = random.randrange(0,4)
        if gamebox[rnum1][rnum2] == 0:
            gamebox[rnum1][rnum2] = 2
            break

def game_win():
    a = 0
    while (a !=3):
        b = 0
        while (b != 3):
            if gamebox[a][b] == 2048:
                break

def gamebox_action_up():
        gamebox_order_up()
        gamebox_merge_up()
        gamebox_order_up()
        gamebox_random()
        #game_win()

def gamebox_action_left():
        gamebox_order_left()
        gamebox_merge_left()
        gamebox_order_left()
        gamebox_random()
        #game_win()

def gamebox_action_down():
        gamebox_order_down()
        gamebox_merge_down()
        gamebox_order_down()
        gamebox_random()
        #game_win()

def gamebox_action_right():
        gamebox_order_right()
        gamebox_merge_right()
        gamebox_order_right()
        gamebox_random()
        #game_win()


#-------------Main------------------------
init()
userinput = None
while (userinput != "quit"):
    gamebox_draw()
    userinput = input("Use WASD to move the blocks:")
    if userinput == 'w':
        gamebox_action_up()
    elif userinput == 'a':
        gamebox_action_left()
    elif userinput == 's':
        gamebox_action_down()
    elif userinput == 'd':
        gamebox_action_right()
    else:
        continue
