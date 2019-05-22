import numpy

# global vars for the board
BOARD_SIZE = 10  # board will be a BOARD_SIZE*BOARD_SIZE matrix
EMPTY = 0
QUEEN = 1


# create an empty BOARD_SIZE*BOARD_SIZE matrix
def create_board():
    return numpy.zeros(shape=(BOARD_SIZE, BOARD_SIZE)).astype(int)


# print board in more user friendly way
def print_board(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            item = board[i][j]
            if item == QUEEN:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print()


def main():
    board = create_board()
    print_board(board)


main()
