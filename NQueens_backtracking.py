import numpy
import itertools as it  # helps to iterate over a loop in two different ranges

# global vars for the board
BOARD_SIZE = 5  # board will be a BOARD_SIZE*BOARD_SIZE matrix
EMPTY = 0
QUEEN = 1
UNDER_ATTACK = 2    # used for testing purposes

# create an empty BOARD_SIZE*BOARD_SIZE matrix
def create_board():
    return numpy.zeros(shape=(BOARD_SIZE, BOARD_SIZE)).astype(int)


# returns true is a square is not attacked by any of the previously placed queen
def is_square_available(board, row, col):

    # check vertical: up
    for i in it.chain(range(0, row)):
        # if board[i][col] == QUEEN:
        #     return False
        if board[i][col] != QUEEN:
            board[i][col] = UNDER_ATTACK

    # check diagonal: left-right
    # upper-part
    r_n = [i for i in range(row - 1, -1, -1)]
    c_n = [i for i in range(col - 1, -1, -1)]
    for i in range(min(len(r_n), len(c_n))):
        # if board[r_n[i]][c_n[i]] == QUEEN:
        #     return False
        if board[r_n[i]][c_n[i]] != QUEEN:
            board[r_n[i]][c_n[i]] = UNDER_ATTACK

    # check diagonal: right-left
    # upper-part
    r_n = [i for i in range(row-1, -1, -1)]
    c_n = [i for i in range(col+1, BOARD_SIZE)]
    for i in range(min(len(r_n), len(c_n))):
        # if board[r_n[i]][c_n[i]] == QUEEN:
        #     return False
        if board[r_n[i]][c_n[i]] != QUEEN:
            board[r_n[i]][c_n[i]] = UNDER_ATTACK

    return True

# print board in more user friendly way
def print_board(board, show_attack = False):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            item = board[i][j]
            if item == QUEEN:
                print("Q", end=" ")
            elif item == UNDER_ATTACK and show_attack:
                print("x", end=" ")
            else:
                print("-", end=" ")
        print()


# pre: row, col must be in range
def place_queen(board, row, col):
    board[row][col] = QUEEN


def solve_NQ(board, col):
    if col >= BOARD_SIZE:
        # means we were able to place a queen in the last col, that's a success
        return True

    for i in range(0, BOARD_SIZE):
        if is_square_available(board, i, col):
            place_queen(board, i, col)
            if solve_NQ(board, col + 1):
                return True

            board[i][col] = EMPTY

    return False




def main():
    board = create_board()

    row = 1; col =3
    board[row][col] = QUEEN
    is_square_available(board,row, col)

    print_board(board, show_attack=True)
    # print(square_is_available(board,6,1))

    # if (solve_NQ(board, 0)):
    #     print_board(board)


main()
