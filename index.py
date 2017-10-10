import random

def display_board(board):
    print('   |   |')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input ('Player 1: Do you want to be X or O').upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    across_the_top = (board[7] == mark and board[8] == mark and board[9] == mark)
    across_the_middle = (board[4] == mark and board[5] == mark and board[6] == mark)
    across_the_bottom = (board[1] == mark and board[2] == mark and board[3] == mark)
    down_the_middle_1 = (board[7] == mark and board[4] == mark and board[1] == mark)
    down_the_middle_2 = (board[8] == mark and board[5] == mark and board[2] == mark)
    down_the_right_side = (board[9] == mark and board[6] == mark and board[3] == mark)
    diagonal_1 = (board[7] == mark and board[5] == mark and board[3] == mark)
    diagonal_2 = (board[9] == mark and board[5] == mark and board[1] == mark)

    return (across_the_top or across_the_middle or across_the_bottom or down_the_middle_1 or down_the_middle_2 or down_the_right_side or diagonal_1 or diagonal_2)

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1':
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True   

def player_choice(board):
    position = ' '
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while position not in numbers or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9)')

    return int(position)

deff replay():
    answer = input('Do you want to play again? Enter Yes or No').lower().startswith('y')
    return answer

while True:
    return False


















