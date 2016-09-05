"""
    Sandbox :: magic_chess_board
        created by Marcus LJX on 2016-06-27
"""

import numpy as np

from puzzles.magic_chessboard.main import init_puzzle_board

BOARDSIZE = 8

loc1 = lambda input: BOARDSIZE * input[0] + input[1]
padbin = lambda input: bin(input)[2:].zfill(BOARDSIZE)


def init_board_0_first(width=BOARDSIZE, height=BOARDSIZE):
    re = np.r_[int(width / 2) * [0, 1]]
    ro = re ^ 1

    return np.row_stack(int(height / 2) * (re, ro))


def init_board_1_first(width=BOARDSIZE, height=BOARDSIZE):
    re = np.r_[int(width / 2) * [1, 0]]
    ro = re ^ 1

    return np.row_stack(int(height / 2) * (re, ro))


def add_boards(b1, b2):
    B = np.zeros((BOARDSIZE, BOARDSIZE), dtype=int)
    for i, row in enumerate(B):
        x = row2num(b1[i]) + row2num(b2[i])
        print(x)
        # row = num2row(row2num(b1) + row2num(b2))

    return B


def num2row(num):
    result = np.zeros(8, dtype=int)
    i = 7
    while i:
        num, r = divmod(num, 2)
        result[i] = r
        i -= 1

    print(result)


def row2num(arr):
    """
    >>> row2num([0,1,0])
    2
    >>> row2num([1,0,0,1,0,1,0,1])
    149

    :param arr:
    :return:
    """
    return sum([arr[x] * (2 ** i) for i, x in enumerate(range(len(arr) - 1, -1, -1))])


def row_as_loc(row):
    S = row2num(row)
    return [(S >> 4) & 0b0111, S & 0b0111]


def show_board_stat(board):
    for row in board:
        x = row2num(row)
        print(row, " \t", x, " \t", padbin(x))


def friend_identify_location(board):
    allegiance = sum(sum(row) for row in board)
    print("allegiance = %d" % allegiance)
    if allegiance >= (BOARDSIZE ** 2) // 2:
        print("black == 1")
        B = init_board_0_first()
    else:
        print("black == 0")
        B = init_board_1_first()

    f = add_boards(B, board)
    # print("After AND op with board")
    # print(f)

    pass


def user_flip(board, loc):
    # flip magic square
    board[loc[0]][loc[1]] = not (board[loc[0]][loc[1]])


#
# def m(board):
#     sum = 0b11111111
#     for row in board:
#         sum += rownum(row)
#         sum = sum % 0b11111111
#         print(padbin(sum), " \t", sum, " \t", row_as_loc(row))





def main():
    board, location = init_puzzle_board()

    print("Jailer sets board.")
    print(board)
    # show_board_stat(board)
    print("Jailer selected location: ", location, " \t", loc1(location), " \t", padbin(loc1(location)))
    print("Value at location is %d" % board[location[0]][location[1]])

    user_flip(board, location)
    print("After user flipped ", location)
    print(board)

    friend_identify_location(board)
    #
    # m(board)


if __name__ == '__main__':
    main()
