import NQueens
from NQueens import *

# vars for n_queens
EMPTY = 0
QUEEN = 1

class Chromosome:
    nQueens = NQueens()
    SIZE = BOARD_SIZE
    body = ""
    fitness = 0.0

    def __init__(self, size = BOARD_SIZE):
        self.SIZE = size
        self.body = self.nQueens.create_empty_board(self.SIZE)
        self.fitness = self.nQueens.get_fitness(self.body,self.SIZE)

    # print a 2D array in a more user friendly way
    def print_chromosome(self):
        print_board(self.body, self.SIZE)
        print(self.fitness)


chromo = Chromosome(6)
chromo.print_chromosome()



