#these modules are needed for the code.
import random
import os
import sys

#------------------------------------
#        Creating the matrix
#------------------------------------
gamebox = list()
gamestate = 'not over'
def init():
    global gamebox
    gamebox = [[0,0,8,2],
            [8,16,32,16],      
            [16,2,512,4],           
            [8,4,1024,4]]
    gamebox_random()

#------------------------------------
#        Drawing the matrix
#------------------------------------
def gamebox_draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0,4):
        for j in range(0,4):
            if j == 3:
               print('\33[33m', '{:4d}'.format(gamebox[i][j]),'\x1b[0m', end="\n"*2)
            else:
               print('\33[33m', '{:4d}'.format(gamebox[i][j]),'\x1b[0m', end=" ")
    print("\n")


#------------------------------------
#  Ordering the items of the matrix
#------------------------------------
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

#------------------------------------
#    Merging the items of the matrix
#------------------------------------
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

#------------------------------------
#  Creating the random number in the matrix
#------------------------------------
def gamebox_random():
    while (True):
        rnum1 = random.randrange(0,4)
        rnum2 = random.randrange(0,4)
        if gamebox[rnum1][rnum2] == 0:
            gamebox[rnum1][rnum2] = 2
            break

#------------------------------------
#      Game states
#------------------------------------

def game_validate():
    global gamestate
    gamestate = 'over'
    game_win()
    gamebox_check_left()
    gamebox_check_right()
    gamebox_check_down()
    gamebox_check_up()
    if gamestate == 'over':
        print("you have lost the game!")
        sys.exit()
 

def game_win():
    a = 0
    while (a !=4):
        b = 0
        while (b !=4):
            if gamebox[a][b] == 2048:
                print ("you have won")
                sys.exit()
            b += 1
        a += 1

def gamebox_check_left():
    global gamestate
    a = 0
    while (a != 4):
        for i in range(0,3):
            for j in range(0,3):
                if gamebox[a][j] == gamebox[a][j+1]:
                    gamestate = 'not over'
                    return gamestate
        a += 1

def gamebox_check_right():
    global gamestate
    a = 0
    while (a != 4):
        for i in range(0,3):
            for j in reversed(range(1,4)):
                if gamebox[a][j] == gamebox[a][j-1]:
                    gamestate = 'not over'
                    return gamestate
        a += 1   

def gamebox_check_down():
    global gamestate
    a = 0
    while (a !=4):
        for j in range(0,3):
                for i in reversed(range(1,4)):
                    if gamebox[i][a] == gamebox[i-1][a]:
                        gamestate = 'not over'
                        return gamestate
        a += 1  

def gamebox_check_up():
    global gamestate
    a = 0
    while (a !=4):
        for j in range(0,3):
                for i in (range(0,3)):
                    if gamebox[i][a] == gamebox[i+1][a]:
                        gamestate = 'not over'
                        return gamestate                
        a += 1

#------------------------------------
#       Matrix actions
#------------------------------------
def gamebox_action_up():
        gamebox_order_up()
        gamebox_merge_up()
        gamebox_order_up()

def gamebox_action_left():
        gamebox_order_left()
        gamebox_merge_left()
        gamebox_order_left()

def gamebox_action_down():
        gamebox_order_down()
        gamebox_merge_down()
        gamebox_order_down()

def gamebox_action_right():
        gamebox_order_right()
        gamebox_merge_right()
        gamebox_order_right()
        

#-----------------------------------------------------------

#------------------------------------
#        Main program
#------------------------------------
init()
userinput = None
while (userinput != "quit"):
    gamebox_random()
    gamebox_draw()
    game_validate()
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