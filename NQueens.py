import numpy as np
import itertools as it  # helps to iterate over a loop in two different ranges

# vars for n_queens

EMPTY = 0
QUEEN = 1

class N_Qqueens:
    # pre: row, col must be in range
    BOARD_SIZE = 0
    def __init__(self, size):
        self.BOARD_SIZE = size

    def place_queen(self, board, row, col):
        board[row][col] = QUEEN

    # pre: row, col must be in range
    def remove_queen(self, board, row, col):
        board[row][col] = EMPTY

    # create an empty BOARD_SIZE*BOARD_SIZE matrix
    def create_empty_board(self):
        return np.zeros(shape=(self.BOARD_SIZE, self.BOARD_SIZE)).astype(int)

    # print board in more user friendly way
    def print_board(self, board):
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                item = board[i][j]
                if item == QUEEN:
                    print("Q", end=" ")
                else:
                    print("-", end=" ")
            print()

    # post: returns number of violations committed in the given locations
    def check_n_violations(self, board, row, col):
        violations = 0
        # check vertical: up
        for i in it.chain(range(0, row)):
            if board[i][col] == QUEEN:
                violations += 1

        # check diagonal: left-right
        # upper-part
        r_n = [i for i in range(row - 1, -1, -1)]
        c_n = [i for i in range(col - 1, -1, -1)]
        for i in range(min(len(r_n), len(c_n))):
            if board[r_n[i]][c_n[i]] == QUEEN:
                violations += 1

        # check diagonal: right-left
        # upper-part
        r_n = [i for i in range(row - 1, -1, -1)]
        c_n = [i for i in range(col + 1, self.BOARD_SIZE)]
        for i in range(min(len(r_n), len(c_n))):
            if board[r_n[i]][c_n[i]] == QUEEN:
                violations += 1

        return violations

    # returns the col index of the queen in the given row, returns -1 if queen not found
    def get_queen_col_index(self, board, row):
        for i in range(self.BOARD_SIZE):
            if board[row][i] == QUEEN:
                return i
        return -1


# post: returns a number between 0-100
    def get_fitness(self, board):
        violations = 0
        for i in range(self.BOARD_SIZE):
            # find the queen in this row
            col = self.get_queen_col_index(board, i)
            # check violations for this queen
            violations += self.check_n_violations(board, i, col)

        # round fitness between 0,100
        violations = max(0, min(violations, self.BOARD_SIZE))  # clip violations between 0-100
        fitness = float(((self.BOARD_SIZE - violations) * 100) / self.BOARD_SIZE)
        return fitness





'''
Testing here
import NQueens

nq = NQueens.N_Qqueens(4)
board = nq.create_empty_board()

nq.place_queen(board,0,2)
nq.place_queen(board,1,0)
nq.place_queen(board,2,3)
nq.place_queen(board,3,1)


nq.print_board(board)
print(nq.get_fitness(board))

result: all testing passed for 4*4
'''