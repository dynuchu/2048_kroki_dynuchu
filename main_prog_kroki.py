import random
import os

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
def gamebox_order():
    i = len(gamebox[0])-1
    print(i)
    inorder = False
    while i >= 1 and not inorder:
        for j in range(1,i):
            if j > game_box[0][j+1]:
                switch = game_box[0][j]
                game_box[0][j] = game_box[0][j+1]
                game_box[0][j+1] = switch
        i = i-1

def gamebox_merge():
    print("action")
def gamebox_random():
    while (True):
        rnum1 = random.randrange(0,4)
        rnum2 = random.randrange(0,4)
        if gamebox[rnum1][rnum2] == 0:
            gamebox[rnum1][rnum2] = 2
            break

init()
userinput = 0
while (gamebox_validate() != False):
    gamebox_draw()
    userinput = input("Use WASD to move the blocks:")
    if userinput == 'w':
        show_list()
    elif userinput == 'a':
        addto_list()
    elif userinput == 's':
        mark_item()
    elif userinput == 'd':
        archive_item()
