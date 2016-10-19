import random
import os

def tab():
    return({
        (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0,
        (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0,
        (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0,
        (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0
    })




def tab_reduct(t,d):
    if d in ('w', 'W'):
        #Merge whitespace
        for _ in range(4):
            for i in range(1,4):
                for c in range(1,5):
                    if t[i+0, c] == 0 and t[i+1, c] !=0:
                        t[i+0, c] = t[i+1,c]
                        t[i+1, c] = 0
        #Merge neighbours
        for i in reversed(range(1,4)):
            for c in range(1,5):
                if t[i+0, c] == t[i+1, c] and t[i,c] != 0:
                    t[i+0, c] *= 2
                    t[i+1, c] = 0
        
        #Merge whitespace
        for _ in range(4):
            for i in range(1,4):
                for c in range(1,5):
                    if t[i+0, c] == 0 and t[i+1, c] !=0:
                        t[i+0, c] = t[i+1,c]
                        t[i+1, c] = 0

def tab_print(t):
    #os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(1,5):
        for c in range(1,5):
            if c == 4:
                print((t[i,c]), end="\n")
            else:
                print((t[i,c]), end=" ")
        
    
    

#~~~~~~~~~~main program~~~~~~~~~~~~
t = tab()
t[(1,4)] = 2
t[(2,4)] = 2
t[(3,4)] = 2
t[(4,4)] = 2
tab_print(t)
arrow = input("Give the next direction (w,a,s,d)")
tab_reduct(t, arrow)
tab_print(t)