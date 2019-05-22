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


# self-note: this function should be updated with several composite funcs for a more clean look
def update_under_attack(board, row, col):
    # update horizontal
    for i in it.chain(range(0, col), range(col + 1, BOARD_SIZE)):
        board[row][i] = UNDER_ATTACK

    # update vertical
    for i in it.chain(range(0, row), range(row + 1, BOARD_SIZE)):
        board[i][col] = UNDER_ATTACK

    # update diagonal: left-right
    # upper-part
    r_n = [i for i in range(row-1, -1, -1)]
    c_n = [i for i in range(col-1, -1, -1)]
    for i in range(min(len(r_n), len(c_n))):
        board[r_n[i]][c_n[i]] = UNDER_ATTACK
    # lower-part
    r_n = [i for i in range(row + 1, BOARD_SIZE)]
    c_n = [i for i in range(col + 1, BOARD_SIZE)]
    for i in range(min(len(r_n), len(c_n))):
        board[r_n[i]][c_n[i]] = UNDER_ATTACK

    # update diagonal: right-left
    # upper-part
    # lower-part

    return board


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


def main():
    board = create_board()

    row = 3; col = 5
    board[row, col] = QUEEN
    update_under_attack(board, row, col)
    print_board(board, show_attack=True)


    # try counting forward
    r_n = [i for i in range(row+1, BOARD_SIZE)]
    c_n = [i for i in range(col+1, BOARD_SIZE)]

    for i in range(min(len(r_n), len(c_n))):
        print(r_n[i], c_n[i])


main()
