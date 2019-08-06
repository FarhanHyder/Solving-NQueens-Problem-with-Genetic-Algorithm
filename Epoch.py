from Chromosome import *


class Epochs:
    chromosomes = []
    sum_of_fitness = 0
    best_fitness = 0

    def __init__(self):
        self.set_initial_population()

    # post: - sets init population
    # - updates sum_of_fitness
    # - updates best_fitness
    def set_initial_population(self):
        for i in range(START_POPULATION):
            c = Chromosome(BOARD_SIZE, randomize=True)
            self.chromosomes.append(c)
            self.sum_of_fitness += c.fitness

            # update best fitness
            if c.fitness > self.best_fitness:
                self.best_fitness = c.fitness

        self.update_selection_probability()

    # pre: sum_of_fitness must be update
    def update_selection_probability(self):
        # update selection probability for each chromosomes in the list
        for chromosome in self.chromosomes:
            chromosome.selection_probability = chromosome.fitness / self.sum_of_fitness

    # post: - returns a selected chromosome index
    #         - ret -1 if no chromosome was selected
    def roulette_wheel_selection(self):
        random_num = uniform(RAND_MIN, RAND_MAX)
        p_probability_sum = 0

        for i in range(len(self.chromosomes)):
            p_probability_sum += self.chromosomes[i].selection_probability
            if (p_probability_sum >= random_num):
                return i
        return -1

    # post: returns a list of tuples [(a,b), (c,d), ...... ]
    def find_pairs(self, arr):
        pairs = []
        # odd length
        if len(arr) % 2 == 1:
            random_idx = randint(1, len(arr) - 1)
            pairs.append((arr.pop(0), random_idx))

        while (len(arr)) > 0:
            parent1 = arr.pop(0)
            parent2 = arr.pop(0)
            pairs.append((parent1, parent2))

        return pairs

    # post: ret a list of selected parents indices
    def select_parents(self):
        parents = []
        num_spins = len(self.chromosomes)
        if NUMBER_OF_SPINS > 0:
            num_spins = NUMBER_OF_SPINS

        print(num_spins)
        for i in range(num_spins):
            parents.append(self.roulette_wheel_selection())

        return parents

    # pre: takes two parent indinces, and the offsprings list
    # post: adds two childs from the crossover process to the offsprings list
    def crossover(self, parent1, parent2, offsprings):
        child1 = Chromosome()
        child2 = Chromosome()

        K = int(BOARD_SIZE / 2)

        # child1 crossover
        # > copy from parent 1
        for i in range(0, K):
            for j in range(BOARD_SIZE):
                # child1[i][j] = parent1[i][j]
                child1.body[i][j] = self.chromosomes[parent1].body[i][j]
        # > copy from parent 2
        for i in range(K, BOARD_SIZE):
            for j in range(BOARD_SIZE):
                # child1[i][j] = parent2[i][j]
                child1.body[i][j] = self.chromosomes[parent2].body[i][j]

        # child2 crossover
        # > copy from parent 2
        for i in range(0, K):
            for j in range(BOARD_SIZE):
                # child2[i][j] = parent2[i][j]
                child2.body[i][j] = self.chromosomes[parent2].body[i][j]
        # copy from parent 1
        for i in range(K, BOARD_SIZE):
            for j in range(BOARD_SIZE):
                # child2[i][j] = parent1[i][j]
                child2.body[i][j] = self.chromosomes[parent1].body[i][j]

        # update fitness for recent borns
        child1.update_fitness()
        child2.update_fitness()

        # add to the existing list
        offsprings.append(child1)
        offsprings.append(child2)


    def mating_season(self):
        offsprings = []
        parents = self.select_parents()
        print("parent: ", parents)                  # delete me
        mating_pairs = self.find_pairs(parents)
        print("mating pairs: ", mating_pairs)       # delete me

        while len(mating_pairs) > 0:
            pair = mating_pairs.pop(0)
            p1 = pair[0];   p2 = pair[1]

            if p1 == p2:
                # can't make children if they are the same person
                offsprings.append(self.chromosomes[p1])
            else:
                self.crossover(p1,p2,offsprings)

        return offsprings


    def print_epoch_info(self):
        print("Total pop.:", len(self.chromosomes), end="\t\t")
        print("Best fitness: ", self.best_fitness, "%", sep="", end="\t\t")
        print("Average fitness: ", (self.sum_of_fitness / len(self.chromosomes)), sep="")

        # TODO : delete this after done
        # for testing purposes



        # testing crossover
        offs = self.mating_season()
        sum = 0
        for i in range(len(offs)):
            # print(offs[i].fitness)
            sum += offs[i].fitness
        print("offs avg. fitness: ",sum/len(offs))



epoch = Epochs()
epoch.print_epoch_info()

# arr = [41, 23, 38, 34, 41, 34, 46, 41, 41, 4, 28, 14, 41, 9, 38, 18, 41, 41, 9, 41, 23, 24, 25]
# print("length ", len(arr))

