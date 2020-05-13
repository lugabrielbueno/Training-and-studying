# TIC TAC TOE GAME

def interf(spaces):
    print(spaces[7]+'|'+spaces[8]+'|'+spaces[9])
    print(spaces[4]+'|'+spaces[5]+'|'+spaces[6])
    print(spaces[1]+'|'+spaces[2]+'|'+spaces[3])

def choice(board, marker, position):
    board[position] = marker

def check_winner(board, mark):
    return ((board[1]==board[2]==board[3]== mark) or
    (board[4]==board[5]==board[6]== mark) or
    (board[7]==board[8]==board[9]== mark) or
    (board[7]==board[4]==board[1]== mark) or
    (board[8]==board[5]==board[2]== mark) or
    (board[9]==board[6]==board[3]== mark) or
    (board[1]==board[5]==board[9]== mark) or
    (board[3]==board[5]==board[7]== mark))

# LETS PLAY THE GAME
test = [' ']*10
interf(test)

player1 = input('Player 1: Choose "X" or "O": ')
if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'

while True:
    
    player1_pos = int(input('Player 1 make your move: [1-9]'))
    choice(test,player1,player1_pos)
    if check_winner(test,player1) == True:
        print('Congratulations player 1, you WIN!')
        break
    interf(test)
    player2_pos = int(input('Player 2 make your move: [1-9]'))
    choice(test,player2,player2_pos)
    if check_winner(test,player2) == True:
        print('Congratulations player 2, you WIN!')
        break
    interf(test)