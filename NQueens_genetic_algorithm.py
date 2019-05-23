import numpy as np
import random
import itertools as it  # helps to iterate over a loop in two different ranges

# vars for n_queens
BOARD_SIZE = 10
EMPTY = 0
QUEEN = 1

# vars for genetic_algo
MAX_EPOCH = 1000
POPULATION = 100  # keep this number even
KILL_SIZE = 30  # percentile values
K = 4


class N_Qqueens:
    # pre: row, col must be in range
    def place_queen(self, board, row, col):
        board[row][col] = QUEEN

    # pre: row, col must be in range
    def remove_queen(self, board, row, col):
        board[row][col] = EMPTY

    # create an empty BOARD_SIZE*BOARD_SIZE matrix
    def create_empty_board(self):
        return np.zeros(shape=(BOARD_SIZE, BOARD_SIZE)).astype(int)

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
        for i in range(BOARD_SIZE):
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
            col = random.randint(0, BOARD_SIZE - 1)  # 0 <= col < BOARD_SIZE
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
        violations = max(0, min(violations, BOARD_SIZE))  # clip violations between 0-100
        fitness = float(((BOARD_SIZE - violations) * 100) / BOARD_SIZE)
        return fitness


class Chromosome_Collection:
    def __init__(self):
        # init by randomly creating some chromosomes
        self.data = []  # contains list of items
        self.BEST_FITNESS = 0
        self.BEST_FIT_CHROMOSOME_INDEX = 0
        self.fitness_data = []

        self.nq = N_Qqueens()
        self.ga = Genetic_Algorithm(self.nq)

        for i in range(POPULATION):
            item = self.get_randomized_item()
            fitness = item[1]
            self.fitness_data.append(fitness)

            if fitness > self.BEST_FITNESS:
                self.BEST_FITNESS = fitness
                self.BEST_FIT_CHROMOSOME_INDEX = i

            self.data.append(item)


    def select_fit_chromosomes(self):
        new_data = []
        fitness_cap = np.percentile(self.fitness_data, KILL_SIZE)

        for i in range(POPULATION):
            if self.data[i][1] > fitness_cap:
                item = []
                chromo = self.data[i][0]
                fitness = self.data[i][1]
                item.append(chromo);    item.append(fitness)

                new_data.append(item)

        parent_population = len(new_data)
        print("parent pop:", parent_population)
        # if parent_population is less than less than 2
        #     we will need one more parent to do mutation
        #     if we have less than 2 parents, then there is huge possibility
        #     that already existing parents have very low fitness, therefore
        #     no need to take those. randomly generate a new chromosome, that will
        #     have the possibility to have a higher fitness
        if parent_population <= 2:
            item = self.get_randomized_item()
            while True:
                if item[1] > fitness_cap:
                    break
                item = self.get_randomized_item()
            new_data.append(item)

        return new_data

    # post: returns two offspring chromosomes
    def crossover(self, parent1, parent2):
        child1 = self.nq.create_empty_board()
        child2 = self.nq.create_empty_board()

        # child1 crossover
            # from parent 1
        for i in range(0, K):
            for j in range(BOARD_SIZE):
                child1[i][j] = parent1[i][j]
            # from parent 2
        for i in range(K, BOARD_SIZE):
            for j in range(BOARD_SIZE):
                child1[i][j] = parent2[i][j]

        # child2 crossover
        # from parent 2
        for i in range(0, K):
            for j in range(BOARD_SIZE):
                child2[i][j] = parent2[i][j]
            # from parent 1
        for i in range(K, BOARD_SIZE):
            for j in range(BOARD_SIZE):
                child2[i][j] = parent1[i][j]


        return child1, child2



    # post: returns an item. item => [chromosome, fitness]
    def get_randomized_item(self):
        item = []  # has the [chromosome, fitness]
        chromo = self.ga.randomize_chromosome()
        fitness = self.ga.get_fitness(chromo)
        item.append(chromo)
        item.append(fitness)

        return item


collection = Chromosome_Collection()
nq = N_Qqueens()
ga = Genetic_Algorithm(nq)


def main():
    nq = N_Qqueens()
    ga = Genetic_Algorithm(nq)
    collection = Chromosome_Collection()

    # testing
    chr = ga.randomize_chromosome()
    nq.print_board(chr)

# crossover
def test6():
    selected = collection.select_fit_chromosomes()

    for i in range(len(selected)):
        print(selected[i][1])


    child1, child2 = collection.crossover(selected[0][0], selected[1][0])
    print("child fitness: ",   ga.get_fitness(child1))
    print("child fitness: ",   ga.get_fitness(child2))





test6()


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

        print("running epoch: ", counter)
        chromo = ga.randomize_chromosome()
        fitness = ga.get_fitness(chromo)

        if fitness == 100:
            nq.print_board(chromo)
            print("A solution found", "        epoch=", counter)
            keep_running = False

        if counter == MAX_EPOCH:
            print("No solution found so far!")
            keep_running = False

        counter += 1


def test4():
    collection = Chromosome_Collection()

    nq = N_Qqueens()
    ga = Genetic_Algorithm(nq)

    for i in range(POPULATION):
        print(collection.data[i][1])

    print()
    print("best fitness: ", collection.BEST_FITNESS)
    print("best fit choromo index: ", collection.BEST_FIT_CHROMOSOME_INDEX)


def test5():
    collection.select_fit_chromosomes()

    for i in range(len(collection.data)):
        print(collection.data[i][1])

