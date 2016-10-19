import random
import os

gamebox = [[0,0,4,2],
            [0,0,8,2],      
            [0,8,2,0],           
            [0,0,8,0]]


def gamebox_draw():
    #os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0,4):
        for j in range(0,4):
            if j == 3:
                print(gamebox[i][j], end="\n")
            else:
                print(gamebox[i][j], end=" ")
    print("\n")

def gamebox_order():
    #balra visz
    for i in range(0,3):
        for j in range(0,3):
            if gamebox[i][j] == 0 and gamebox[i][j+1] !=0:
                gamebox[i][j] = gamebox[i][j+1]
                gamebox[i][j+1] = 0

    

def gamebox_merge():
    print("merge")
def gamebox_action():
    print("action")
    gamebox_order()




def gamebox_random():
    print("random")

def gamebox_validate():
    print("validate")

    
    

#~~~~~~~~~~main program~~~~~~~~~~~~

gamebox_draw()
gamebox_order()
gamebox_draw()