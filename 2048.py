game_box = [[0,2,2,0],
            [0,0,0,0],      
            [0,0,0,0],           
            [0,0,0,0]]

def game_box_draw():
    for i in range(0,4):
        for j in range(0,4):
            if j == 3:
                print(game_box[i][j], end="\n")
            else:
                print(game_box[i][j], end=" ")

def switch_function():
    i = len(game_box[0])-1
    print(i)
    inorder = False
    while i >= 1 and not inorder:
       # inorder = True
        for j in range(1,i):
            if j > game_box[0][j+1]:
                switch = game_box[0][j]
                game_box[0][j] = game_box[0][j+1]
                game_box[0][j+1] = switch
        i = i-1
    game_box_draw()

#main program
game_box_draw()
switch_function()