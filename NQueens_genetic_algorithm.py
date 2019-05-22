import numpy
import random
import itertools as it  # helps to iterate over a loop in two different ranges


MAX_EPOCH = 100
BOARD_SIZE = 10
EMPTY = 0
QUEEN = 1


class N_Qqueens:
    # pre: row, col must be in range
    def place_queen(self, board, row, col):
        board[row][col] = QUEEN

    # pre: row, col must be in range
    def remove_queen(self, board, row, col):
        board[row][col] = EMPTY

    # create an empty BOARD_SIZE*BOARD_SIZE matrix
    def create_empty_board(self):
        return numpy.zeros(shape=(BOARD_SIZE, BOARD_SIZE)).astype(int)

    # print board in more user friendly way
    def print_board(self, board):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                item = board[i][j]
                if item == QUEEN:
                    print("Q", end=" ")
                else:
                    print("-", end=" ")
            print()

    # post: returns true if a rule is violated for the current position, false otherwise
    def check_violation(self, board, row, col):
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


class Genetic_Algorithm:
    # def __init__(self, NQ):
    #     self.nq = NQ

    def randomize_chromosome(self):
        nq = N_Qqueens()
        chr = nq.create_empty_board()
        # randomly place a queen in each row
        for i in range(BOARD_SIZE):
            col = random.randint(0,BOARD_SIZE-1)    # 0 <= col < BOARD_SIZE
            nq.place_queen(chr, i, col)

        return chr

    # post: returns a number between 0-100
    def find_fitness(self, board):
        violations = 0



def main():
    ga = Genetic_Algorithm()
    nq = N_Qqueens()

    # testing
    chr = ga.randomize_chromosome()
    nq.print_board(chr)




main()
# for i in range(BOARD_SIZE):
#     print(random.randint(0,BOARD_SIZE-1))