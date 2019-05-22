import numpy
import random
import itertools as it  # helps to iterate over a loop in two different ranges

# vars for n_queens
BOARD_SIZE = 10
EMPTY = 0
QUEEN = 1

# vars for genetic_algo
MAX_EPOCH = 1000
POPULATION = 20
KILL_SIZE = 50  # in percentage
K = int(BOARD_SIZE/2)


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

    # post: returns number of violations committed in the given locations
    def check_violation(self, board, row, col):
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
        c_n = [i for i in range(col + 1, BOARD_SIZE)]
        for i in range(min(len(r_n), len(c_n))):
            if board[r_n[i]][c_n[i]] == QUEEN:
                violations += 1

        return violations

    # returns the col index of the queen in the given row, returns -1 if queen not found
    def get_queen_col_index(self, board, row):
        for i in range (BOARD_SIZE):
            if board[row][i] == QUEEN:
                return i
        return -1


    # remove following later
    def is_square_available(self, board, row, col):
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

    def is_solution_found(self, board, row=0):
        if row >= BOARD_SIZE:
            # means we were able to place a queen in the last row (board[BOARD_SIZE-1][some_col]), that's a success
            return True

        for i in range(0, BOARD_SIZE):
            if self.is_square_available(board, row, i):
                # square is available, place queen
                self.place_queen(board, row, i)
                # recursive call and place queen in the next row
                # as there is constraint to placing queen in the same row
                if self.is_solution_found(board, row + 1):
                    return True

                # placing the queen here didn't work. so remove it and backtrack to previous step.
                self.remove_queen(board, row, i)

        return False


class Genetic_Algorithm:
    def __init__(self, NQ):
        self.nq = NQ

    def randomize_chromosome(self):
        chr = self.nq.create_empty_board()
        # randomly place a queen in each row
        for i in range(BOARD_SIZE):
            col = random.randint(0,BOARD_SIZE-1)    # 0 <= col < BOARD_SIZE
            self.nq.place_queen(chr, i, col)

        return chr

    # post: returns a number between 0-100
    def get_fitness(self, board):
        violations = 0
        for i in range(BOARD_SIZE):
            # find the queen in this row
            col = self.nq.get_queen_col_index(board, i)
            # check violations for this queen
            violations += self.nq.check_violation(board, i, col)

        # round fitness between 0,100
        violations = max(0, min(violations, BOARD_SIZE)) # clip violations between 0-100
        fitness = float(((BOARD_SIZE-violations)*100)/BOARD_SIZE)
        return fitness

class Chromosome_Collection:
    def __init__(self):
        # init by randomly creating some chromosomes
        self.data = []      # contains list of items
        self.BEST_FITNESS = 0
        self.BEST_FIT_CHROMOSOME_INDEX = 0

        self.nq = N_Qqueens()
        self.ga = Genetic_Algorithm(self.nq)

        for i in range(POPULATION):
            item = []   # has the [chromosome, fitness]
            chromo = self.ga.randomize_chromosome()
            fitness = self.ga.get_fitness(chromo)
            item.append(chromo);    item.append(fitness)

            if fitness > self.BEST_FITNESS:
                self.BEST_FITNESS = fitness
                self.BEST_FIT_CHROMOSOME_INDEX = i

            self.data.append(item)



def main():
    nq = N_Qqueens()
    ga = Genetic_Algorithm(nq)

    # testing
    chr = ga.randomize_chromosome()
    nq.print_board(chr)

def test4():
    collection = Chromosome_Collection()

    nq = N_Qqueens()
    ga = Genetic_Algorithm(nq)

    for i in range(POPULATION):
        print(collection.data[i][1])

    print()
    print("best fitness: ", collection.BEST_FITNESS)
    print("best fit choromo index: ", collection.BEST_FIT_CHROMOSOME_INDEX)

test4()
# main()






def test():
    nq = N_Qqueens()
    ga = Genetic_Algorithm(nq)

    chr = ga.randomize_chromosome()
    nq.print_board(chr)
    print(ga.get_fitness(chr))

def test2():
    nq = N_Qqueens()
    board = nq.create_empty_board()

    if nq.is_solution_found(board):
        nq.print_board(board)
    else:
        print("Solution Not Found!")

    ga = Genetic_Algorithm(nq)
    chr = ga.randomize_chromosome()

    # nq.print_board(board)
    print(ga.get_fitness(board))

    nq.print_board(chr)
    print(ga.get_fitness(chr))

# test fitness
def test3():
    nq = N_Qqueens()
    ga = Genetic_Algorithm(nq)

    keep_running = True

    counter = 1
    while keep_running:

        print("running epoch: ",counter)
        chromo = ga.randomize_chromosome()
        fitness = ga.get_fitness(chromo)

        if fitness == 100:
            nq.print_board(chromo)
            print("A solution found", "        epoch=",counter)
            keep_running = False

        if counter == MAX_EPOCH:
            print("No solution found so far!")
            keep_running = False

        counter += 1