import random

board = ['-','-','-','-','-','-','-','-','-',]
sidewin = [0,1,2]
upwin = [0,3,6]
diagwin = [0,4,8]
placestocheck = [0,1,2,3,6]

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
    sidewincountO = 0
    sidewincountX = 0
    upwincountO = 0
    upwincountX = 0
    diagwincountO = 0
    diagwincountX = 0
    for i in placestocheck:
        for j in sidewin:
            if board[i + j] == 'X':
                sidewincountX += 1
            elif board[i + j] == 'O':
                sidewincountO += 1
            else:
                sidewincountX = 0
                sidewincountO = 0
                break

        for k in upwin:
            if board[i + k] == 'X':
                upwincountX += 1
            elif board[i + k] == 'O':
                upwincountO += 1
            else:
                upwincountX = 0
                upwincountO = 0
                break
                
        for l in diagwin:
            if board[i + l] == 'X':
                diagwincountX += 1
            elif board[i + l] == 'O':
                diagwincountO += 1
            else:
                diagwincountX = 0
                diagwincountO = 0
                break
        if diagwincountX == 3 or sidewincountX == 3 or upwincountX == 3: 
            print('well done you won')
            exit()
        elif diagwincountO == 3 or sidewincountO == 3 or upwincountO == 3: 
            print('U idiot you lost to a randomisation bot')
            exit()

def completemoves():
    pmove()
    cmove()

while True:
    printboard()
    completemoves()
    windetect()
