from NQueens import *
from random import randint, uniform



class Chromosome:
    nQueens = NQueens()
    SIZE = BOARD_SIZE
    body = ""                       # n*n matrix
    fitness = 0.0                   # [0.0, 100.0]
    selection_probability = 0       # [0.0, 1]

    def __init__(self, size = BOARD_SIZE, randomize = False):
        self.SIZE = size
        self.body = self.nQueens.create_empty_board(self.SIZE)

        if randomize:
            # randomly place a queen in each row
            for i in range(self.SIZE):
                col = randint(0, self.SIZE - 1)  # 0 <= col < BOARD_SIZE
                self.nQueens.place_queen(self.body, i, col)

        self.fitness = self.nQueens.get_fitness(self.body,self.SIZE)

    # print a 2D array in a more user friendly way
    def print_chromosome(self):
        print_board(self.body, self.SIZE, msg="[ Body ]")
        print("fitness : ",self.fitness,"%",sep="")

#
# chromo = Chromosome(6, randomize=True)
# chromo.print_chromosome()


