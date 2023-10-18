board = [" " for i in range(9)]
icon = 'X'
end_game = False

def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])
    
    print(row1)
    print(row2)
    print(row3)
        
        
def player_move():
    global icon
    if icon == 'X':
        number = 1
    else: 
        number = 2
    
    print("Your turn Player {}".format(number))
    
    choice = int(input('Enter your move (1-9): '))
    if board[choice-1] == ' ':
        board[choice - 1] = icon
        
        check_winner(icon)
        check_draw()
        
        if icon == 'X':
            icon = 'O'
        else:
            icon = 'X'
            

    else:
        print('That space is taken')
    print_board()


def check_winner(icon):
    global end_game
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        print('{} wins! Congratulations!'.format(icon)) 
        end_game = True

def check_draw():
    global end_game
    if " " not in board:
        print("It's a draw!")
        end_game = True


while True:
    player_move()
    if end_game:
        break

    

    
