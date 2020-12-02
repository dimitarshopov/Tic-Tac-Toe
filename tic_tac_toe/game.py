from tic_tac_toe.printing import print_board, print_game_over, print_welcome
from tic_tac_toe.setup import setup

BOARD_SIZE = 3


def chooses_position(board, player):
    position = int(input(f'{player.name} chooses a free position [1-9]: '))
    row = (position - 1) // BOARD_SIZE
    col = (position - 1) % BOARD_SIZE
    board[row][col] = player.mark


def all_single_values(ll, value):
    for v in ll:
        if v != value:
            return False
    return True


def check_game_over(board, player):
    row_checks = [all_single_values(row, player.mark) for row in board]
    columns = [[board[i][j] for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
    column_checks = [all_single_values(column, player.mark) for column in columns]
    diagonals = [
        [board[i][i] for i in range(BOARD_SIZE)],
        [board[i][BOARD_SIZE - i - 1] for i in range(BOARD_SIZE)]
    ]
    diagonals_check = [all_single_values(diagonal, player.mark) for diagonal in columns]

    all_checks = [
        *row_checks,
        *column_checks,
        *diagonals_check
    ]
    return any(all_checks)


def game_loop(board, players):
    current_player, next_player = players
    while True:
        print_board(board)
        chooses_position(board, current_player)
        if check_game_over(board, current_player):
            print_game_over(board, current_player)
            break
        current_player, next_player = next_player, current_player


def start_game(board_size):
    (board, *players) = setup(board_size)
    print_welcome(players[0])
    # print_board(board)
    # print(players)
    game_loop(board, players)