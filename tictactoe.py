import random

board = ['-','-','-','-','-','-','-','-','-',]
sidewin = []
upwin = []
diagwin = []

def printboard():
    print(board[0], end='')
    print('|', end='')
    print(board[1], end='')
    print('|', end='')
    print(board[2])
    print(board[3], end='')
    print('|', end='')
    print(board[4], end='')
    print('|', end='')
    print(board[5])
    print(board[6], end='')
    print('|', end='')
    print(board[7], end='')
    print('|', end='')
    print(board[8])

def pmove():
    loopagain = True
    while loopagain:
        pmove = input('Where do you want to place an X')
        pmove = int(pmove)
        pmove -= 1
        if board[pmove] == 'X':
            loopagain = True
        elif board[pmove] == 'O':
            loopagain = True
        else:
            loopagain = False
    board[pmove] = 'X'

def cmove():
    loopagain = True
    while loopagain:
        cmove = random.randint(0, 8)
        if board[cmove] == 'X':
            loopagain = True
        elif board[cmove] == 'O':
            loopagain = True
        else:
            loopagain = False
    board[cmove] = 'O'

def windetect():
    for i in range(8):
        for j in sidewin:
            if board[i + j] == 'X':
                sidewincount += 1
            else:
                sidewincount = 0
                break
    
        
        for k in upwin:

        for l in diagwin:
        
        

def completemoves():
    cmove()
    pmove()




while True:
    printboard()
    completemoves()
