import numpy
import itertools as it  # helps to iterate over a loop in two different ranges

# global vars for the board
BOARD_SIZE = 25  # board will be a BOARD_SIZE*BOARD_SIZE matrix
# in order to try different try different chessboards, change BOARD_SIZE

EMPTY = 0
QUEEN = 1
UNDER_ATTACK = 2  # used for testing purposes


# create an empty BOARD_SIZE*BOARD_SIZE matrix
def create_board():
    return numpy.zeros(shape=(BOARD_SIZE, BOARD_SIZE)).astype(int)


# returns true is a square is not attacked by any of the previously placed queen
def is_square_available(board, row, col):
    # check vertical: up
    for i in it.chain(range(0, row)):
        if board[i][col] == QUEEN:
            return False

    # check diagonal: left-right
    # upper-part
    r_n = [i for i in range(row - 1, -1, -1)]
    c_n = [i for i in range(col - 1, -1, -1)]
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


# pre: row, col must be in range
def remove_queen(board, row, col):
    board[row][col] = EMPTY


# pre: upon it's main call,
# post: returns if a solution is available for a given board
def is_solution_found(board, row=0):
    if row >= BOARD_SIZE:
        # means we were able to place a queen in the last row (board[BOARD_SIZE-1][some_col]), that's a success
        return True

    for i in range(0, BOARD_SIZE):
        if is_square_available(board, row, i):
            # square is available, place queen
            place_queen(board, row, i)
            # recursive call and place queen in the next row
            # as there is constraint to placing queen in the same row
            if is_solution_found(board, row + 1):
                return True

            # placing the queen here didn't work. so remove it and backtrack to previous step.
            remove_queen(board, row, i)

    return False


def main():
    board = create_board()

    if is_solution_found(board):
        print_board(board)
    else:
        print("Solution Not Found!")


main()
