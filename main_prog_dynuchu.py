import random
import os

gamebox = [[0,0,0,0],
            [0,2,2,0],      
            [0,8,2,0],           
            [2,2,0,0]]


def gamebox_draw():
    #os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0,4):
        for j in range(0,4):
            if j == 3:
                print(gamebox[i][j], end="\n")
            else:
                print(gamebox[i][j], end=" ")
    print("\n")

def gamebox_order_bal():
    #balra visz
    a = 0
    while (a != 4):
        for i in range(0,3):
            for j in range(0,3):
                if gamebox[a][j] == 0 and gamebox[a][j+1] !=0:
                    gamebox[a][j] = gamebox[a][j+1]
                    gamebox[a][j+1] = 0
        a += 1

def gamebox_order_jobb():
    #balra visz
    a = 0
    while (a != 4):
        for i in range(0,3):
            for j in reversed(range(1,4)):
                if gamebox[a][j] == 0 and gamebox[a][j-1] !=0:
                    gamebox[a][j] = gamebox[a][j-1]
                    gamebox[a][j-1] = 0
        a += 1

def gamebox_order_fel():
    a = 0
    while (a !=4):
        for j in range(0,3):
                for i in (range(0,3)):
                    if gamebox[i][a] == 0 and gamebox[i+1][a] !=0:
                        gamebox[i][a] = gamebox[i+1][a]
                        gamebox[i+1][a] = 0
        a += 1

def gamebox_order_le():
    a = 0
    while (a !=4):
        for j in range(0,3):
                for i in reversed(range(1,4)):
                    if gamebox[i][a] == 0 and gamebox[i-1][a] !=0:
                        gamebox[i][a] = gamebox[i-1][a]
                        gamebox[i-1][a] = 0
        a += 1

def gamebox_merge_balra():
    a = 0
    while (a != 4):
        for i in range(0,3):
            for j in range(0,3):
                if gamebox[a][j] == gamebox[a][j+1] and gamebox[a][j] !=0:
                    gamebox[a][j] *= 2
                    gamebox[a][j+1] = 0
        a += 1                

def gamebox_merge_jobbra():
    a = 0
    while (a != 4):
        for i in range(0,3):
            for j in reversed(range(1,4)):
                if gamebox[a][j] == gamebox[a][j-1] and gamebox[a][j] !=0:
                    gamebox[a][j] *= 2
                    gamebox[a][j-1] = 0
        a += 1   

def gamebox_merge_fel():
    a = 0
    while (a !=4):
        for j in range(0,3):
                for i in (range(0,3)):
                    if gamebox[i][a] == gamebox[i+1][a] and gamebox[i][a]!=0: 
                        gamebox[i][a] *= 2
                        gamebox[i+1][a] = 0
        a += 1


def gamebox_merge_le():
    a = 0
    while (a !=4):
        for j in range(0,3):
                for i in reversed(range(1,4)):
                    if gamebox[i][a] == gamebox[i-1][a] and gamebox[i][a] !=0:
                        gamebox[i][a] *= 2
                        gamebox[i-1][a] = 0
        a += 1


def gamebox_action_bal():
    gamebox_order_bal()
    gamebox_merge_balra()
    gamebox_order_bal()

def gamebox_action_jobb():
    gamebox_order_jobb()
    gamebox_merge_jobbra()
    gamebox_order_jobb():

def gamebox_action_fel():
    gamebox_order_fel()
    gamebox_merge_fel()
    gamebox_order_fel()

def gamebox_action_le():
    gamebox_order_le()
    gamebox_merge_le()
    gamebox_order_le()




def gamebox_random():
    print("random")

def gamebox_validate():
    print("validate")

    
    

#~~~~~~~~~~main program~~~~~~~~~~~~

gamebox_draw()
gamebox_action_bal()
gamebox_draw()


