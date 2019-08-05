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


    def print_epoch_info(self):
        print("Total pop.:", len(self.chromosomes), end="\t\t")
        print("Best fitness: ", self.best_fitness, "%", sep="", end="\t\t")
        print("Average fitness: ", (self.sum_of_fitness / len(self.chromosomes)), sep="")

        # TODO : delete this after done
        # for testing purposes
        parents = self.select_parents()
        print("parent: ", parents)
        mating_pairs = self.find_pairs(parents)
        print("mating pairs: ", mating_pairs)



epoch = Epochs()
# # epoch.test_selection()
epoch.print_epoch_info()

# arr = [41, 23, 38, 34, 41, 34, 46, 41, 41, 4, 28, 14, 41, 9, 38, 18, 41, 41, 9, 41, 23, 24, 25]
# print("length ", len(arr))
