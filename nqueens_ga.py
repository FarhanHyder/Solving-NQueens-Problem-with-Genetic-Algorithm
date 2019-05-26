import itertools as it  # helps to iterate over a loop in two different ranges
import numpy as np
import random

START_POPULATION = 70
BOARD_SIZE = 6

class Chromosome:
    def __init__(self,c_data = 0, fitness_score = 0, randomize = False):
        if randomize:
            # default constructor
            chromo = self.randomize_chromosome()
            self.c_data = chromo.c_data
            self.fitness_score = chromo.fitness_score
        else:
            # constructor with params
            self.c_data = c_data
            self.fitness_score = fitness_score

    # post: returns a randomized Chromosome
        # that might have a few nq violations
    def randomize_chromosome(self):
        nq = N_queens()
        c_data = nq.create_empty_board()
        # randomly place a queen in each row
        for i in range(BOARD_SIZE):
            col = random.randint(0, BOARD_SIZE - 1)  # 0 <= col < BOARD_SIZE
            nq.place_queen(c_data, i, col)

        fitness_score = nq.get_fitness_score(c_data)

        return Chromosome(c_data, fitness_score)

    def print_chromosome(self):
        nq = N_queens()
        print("Chromosome data:")
        nq.print_board(self.c_data)
        print("Chromosome fitness score: ", round(self.fitness_score, 2))


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

    # returns the col index of the queen in the given row, returns -1 if queen not found
    def get_queen_col_index(self, board, row):
        for i in range(BOARD_SIZE):
            if board[row][i] == self.QUEEN:
                return i
        return -1

    # post: returns a number between 0-100
    def get_fitness_score(self, board):
        violations = 0
        for i in range(BOARD_SIZE):
            # find the queen in this row
            col = self.get_queen_col_index(board, i)
            # check violations for this queen
            violations += self.check_violation(board, i, col)

        # round fitness between 0,100
        violations = max(0, min(violations, BOARD_SIZE))  # clip violations between 0-100
        fitness = float(((BOARD_SIZE - violations) * 100) / BOARD_SIZE)
        return fitness

class Epoch:
    def __init__(self):
        self.data = []
        self.BEST_FITNESS = 0
        self.BEST_FIT_CHROMOSOME_INDEX = 0
        self.fitness_data = []

    def init_first_epoch(self):
        pass



def test_randomize_chromosome():
    chromo = Chromosome(randomize=True)
    chromo.print_chromosome()
test_randomize_chromosome()


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
# test_nq()

