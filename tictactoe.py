import random

board = ['-','-','-','-','-','-','-','-','-',]

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
        if board[pmove] == 'X':
            loopagain = True
        elif board == 'O':
            loopagain = True
        else:
            loopagain = False
    return pmove

def cmove():
    loopagain = True
    while loopagain:
        cmove = random.randint(0, 8)
        if board[cmove] == 'X':
            loopagain = True
        elif board == 'O':
            loopagain = True
        else:
            loopagain = False
    return cmove

def commitmove(pmove, cmove):
    board[pmove] = 'X'
    board[cmove] = 'O'

while True:
    printboard()
    commitmove(pmove(), cmove())