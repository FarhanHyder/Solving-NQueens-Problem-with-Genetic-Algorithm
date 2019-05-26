import itertools as it  # helps to iterate over a loop in two different ranges
import numpy as np



START_POPULATION = 70
BOARD_SIZE = 5

class Chromosome:
    def __init__(self,c_data, fitness_score):
        self.c_data = c_data
        self.fitness_score = fitness_score

class N_queens:
    QUEEN = 1
    EMPTY = 0

    # pre: row, col must be in range
    def place_queen(self, board, row, col):
        board[row][col] = self.QUEEN

    # pre: row, col must be in range
    def remove_queen(self, board, row, col):
        board[row][col] = self.EMPTY

    # create an empty BOARD_SIZE*BOARD_SIZE matrix
    def create_empty_board(self):
        return np.zeros(shape=(BOARD_SIZE, BOARD_SIZE)).astype(int)

    # print board in more user friendly way
    def print_board(self, board):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                item = board[i][j]
                if item == self.QUEEN:
                    print("Q", end=" ")
                else:
                    print("-", end=" ")
            print()

    # post: returns number of violations committed in the given locations
    def check_violation(self, board, row, col):
        violations = 0
        # check vertical: up
        for i in it.chain(range(0, row)):
            if board[i][col] == self.QUEEN:
                violations += 1

        # check diagonal: left-right
        # upper-part
        r_n = [i for i in range(row - 1, -1, -1)]
        c_n = [i for i in range(col - 1, -1, -1)]
        for i in range(min(len(r_n), len(c_n))):
            if board[r_n[i]][c_n[i]] == self.QUEEN:
                violations += 1

        # check diagonal: right-left
        # upper-part
        r_n = [i for i in range(row - 1, -1, -1)]
        c_n = [i for i in range(col + 1, BOARD_SIZE)]
        for i in range(min(len(r_n), len(c_n))):
            if board[r_n[i]][c_n[i]] == self.QUEEN:
                violations += 1

        return violations

class Epoch:
    def __init__(self):
        self.data = []
        self.BEST_FITNESS = 0
        self.BEST_FIT_CHROMOSOME_INDEX = 0
        self.fitness_data = []

    def init_first_epoch(self):
        pass



def test_nq():
    nq = N_queens()
    board = nq.create_empty_board()
    print("Test: adding stuffs")
    nq.place_queen(board,1,3)
    nq.place_queen(board,3,1)
    nq.print_board(board)

    print()
    print("Test: removing stuff")
    nq.remove_queen(board, 3,1)
    nq.print_board(board)
test_nq()

