import numpy as np
import random
import itertools as it  # helps to iterate over a loop in two different ranges

# vars for n_queens
BOARD_SIZE = 10
EMPTY = 0
QUEEN = 1

# vars for genetic_algo
MAX_EPOCH = 100
POPULATION = 100  # keep this number even
KILL_SIZE = 40  # percentile values
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


class Genetic_Algorithm_Util:
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

    # post: returns if a number is odd
    def is_odd(self, num):
        return (num%2 == 1)




class Chromosome_Collection:
    def __init__(self):
        # init by randomly creating some chromosomes
        self.data = []  # contains list of items
        self.BEST_FITNESS = 0
        self.BEST_FIT_CHROMOSOME_INDEX = 0
        self.fitness_data = []

        self.nq = N_Qqueens()
        self.ga = Genetic_Algorithm_Util(self.nq)

        for i in range(POPULATION):
            item = self.get_randomized_item()
            fitness = item[1]
            self.fitness_data.append(fitness)

            if fitness > self.BEST_FITNESS:
                self.BEST_FITNESS = fitness
                self.BEST_FIT_CHROMOSOME_INDEX = i

            self.data.append(item)

    def update_new_data_info(self, new_data):
        new_best_fitness = 0
        new_best_fit_chromo_idx = 0
        new_fitness_data = []

        for i in range(POPULATION):
            fitness = new_data[i][1]
            new_fitness_data.append(fitness)

            if fitness > new_best_fitness:
                new_best_fitness = fitness
                new_best_fit_chromo_idx = i

        self.data = new_data
        self.BEST_FITNESS = new_best_fitness
        self.BEST_FIT_CHROMOSOME_INDEX = new_best_fit_chromo_idx
        self.fitness_data = new_fitness_data


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

    def data_info(self, s):
        print(s,end="\t\t\t")
        print("best fitness:",self.BEST_FITNESS)


    # post: returns two offspring chromosome items
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

        i1 = []; i2 = []
        i1.append(child1)
        i1.append(self.ga.get_fitness(child1))
        i2.append(child2)
        i2.append(self.ga.get_fitness(child2))

        return i1, i2

    # post: returns index number of two parents
    def select_parents(self, parent_list_size):
        # randomly select two parents
        parent1 = random.randint(0,parent_list_size-1)
        parent2 = -1
        while True:
            parent2 = random.randint(0,parent_list_size-1)
            if parent2 != parent1:
                break

        return parent1, parent2

    # post: returns an item. item => [chromosome, fitness]
    def get_randomized_item(self):
        item = []  # has the [chromosome, fitness]
        chromo = self.ga.randomize_chromosome()
        fitness = self.ga.get_fitness(chromo)
        item.append(chromo)
        item.append(fitness)

        return item

    def epoch(self):

        selected_chromosomes  = self.select_fit_chromosomes()
        offspring_needed = POPULATION - len(selected_chromosomes)
        offsprings = []

        counter = 0
        while (counter < offspring_needed):
            p1_idx, p2_idx = self.select_parents(len(selected_chromosomes))
            parent1 = selected_chromosomes[p1_idx][0]
            parent2 = selected_chromosomes[p2_idx][0]
            child1, child2 = self.crossover(parent1,parent2)

            offsprings.append(child1)
            offsprings.append(child2)

            counter += 2

        new_data = []

        if ga.is_odd(offspring_needed):
            new_data = selected_chromosomes+offsprings[:len(offsprings)-1]
        else:
            new_data = selected_chromosomes + offsprings

        self.update_new_data_info(new_data)

    def run(self):
        counter = 0
        while True:
            self.data_info("epoch ["+str(counter)+"]")
            self.epoch()
            if self.BEST_FITNESS == 100:
                print("Solution found!")
                break
            if counter == MAX_EPOCH:
                print("Solution not found!")
                break

            counter += 1









collection = Chromosome_Collection()
nq = N_Qqueens()
ga = Genetic_Algorithm_Util(nq)


def main():
    nq = N_Qqueens()
    ga = Genetic_Algorithm_Util(nq)
    collection = Chromosome_Collection()

    # testing
    collection.sort_by_fitness()


def test_run():
    collection.run()

test_run()

def test_epoch():
    collection.data_info()
    collection.epoch()
    print()
    collection.data_info()

# test_epoch()



def test_cross():
    selected = collection.select_fit_chromosomes()
    c1, c2 = collection.crossover(selected[0][0], selected[1][0])

    print("child1 fitness: ",c1[1])
    print("child2 fitness: ",c2[1])

# test_cross()