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

printboard()