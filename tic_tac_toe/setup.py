from tic_tac_toe.Player import Player



def setup_board(size):
    return [[None] * size for _ in range(size)]


def setup_player(mark=None):
    name = input('Name: ')
    if not mark:
        mark = input('Mark: ')
    else:
        print(f'Mark: {mark}')
    return Player(name, mark)


def setup(board_size):
    player_one = setup_player()
    player_two = setup_player('0' if player_one.mark == 'X' else '0')
    board = setup_board(board_size)

    return (board, player_one, player_two)