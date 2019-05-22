import numpy
import itertools as it  # helps to iterate over a loop in two different ranges

# global vars for the board
BOARD_SIZE = 10  # board will be a BOARD_SIZE*BOARD_SIZE matrix
EMPTY = 0
QUEEN = 1
UNDER_ATTACK = 2  # if a position is marked UNDER_ATTACK, then it is not safe to play in that pos


# create an empty BOARD_SIZE*BOARD_SIZE matrix
def create_board():
    return numpy.zeros(shape=(BOARD_SIZE, BOARD_SIZE)).astype(int)


# returns true is a square is not attacked by any of the previously placed queen
def square_is_available(board, row, col):
    # check horizontal
    for i in it.chain(range(0, col), range(col + 1, BOARD_SIZE)):
        if board[row][i] == QUEEN:
            return False

    # check vertical: up
    for i in it.chain(range(0, row)):
        if board[i][col] == QUEEN:
            return False

    # check diagonal: left-right
        # upper-part
    r_n = [i for i in range(row-1, -1, -1)]
    c_n = [i for i in range(col-1, -1, -1)]
    for i in range(min(len(r_n), len(c_n))):
        if board[r_n[i]][c_n[i]] == QUEEN:
            return False

    # check diagonal: right-left
        # upper-part
    r_n = [i for i in range(row - 1, -1, -1)]
    c_n = [i for i in range(col + 1, BOARD_SIZE)]
    for i in range(min(len(r_n), len(c_n))):
        if board[r_n[i]][c_n[i]] == QUEEN:
            return False

    return True


# print board in more user friendly way
def print_board(board, show_attack=False):
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
    update_under_attack(board,row,col)


def main():
    board = create_board()

    # place_queen(board,1,3)
    place_queen(board,6,5)
    print_board(board, show_attack=True)


main()