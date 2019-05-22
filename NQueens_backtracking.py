import numpy

# global vars for the board
BOARD_SIZE = 10  # board will be a BOARD_SIZE*BOARD_SIZE matrix
EMPTY = 0
QUEEN = 1
UNDER_ATTACK = 2    # if a position is marked UNDER_ATTACK, then it is not safe to play in that pos


# create an empty BOARD_SIZE*BOARD_SIZE matrix
def create_board():
    return numpy.zeros(shape=(BOARD_SIZE, BOARD_SIZE)).astype(int)

def update_under_attack(board,row,col):
    # update horizontal
    for i,j in zip(range(0,row), range(row+1, BOARD_SIZE)):
        board[i][j] = UNDER_ATTACK

    return board

# print board in more user friendly way
def print_board(board, show_attack=False):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            item = board[i][j]
            if item == QUEEN:
                print("Q", end=" ")
            elif item == UNDER_ATTACK and show_attack:
                print("A", end=" ")
            else:
                print("-", end=" ")
        print()


def main():
    board = create_board()

    board[5,5] = QUEEN
    update_under_attack(board,5,5)
    print_board(board, True)

main()
