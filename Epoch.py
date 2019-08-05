from Chromosome import *


class Epoch:
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

    # returns a selected chromosome
    def roulette_wheel_selection(self):
        random_num = uniform(RAND_MIN, RAND_MAX)
        p_probability_sum = 0
        selected_chromosome_idx = -1

        for i in range(len(self.chromosomes)):
            p_probability_sum += self.chromosomes[i].selection_probability
            if (p_probability_sum >= random_num):
                selected_chromosome_idx = i

        return self.chromosomes[selected_chromosome_idx]

    def select_parents(self):
        parents = []
        for i in range(len(self.chromosomes)):
            parents.append(self.roulette_wheel_selection())

        return parents


    def print_epoch_info(self):
        print("Total pop.:",len(self.chromosomes),end="\t\t")
        print("Best fitness: ",self.best_fitness,"%",sep="",end="\t\t")
        print("Average fitness: ",(self.sum_of_fitness / len(self.chromosomes)),sep="")

        # TODO : delete this after done
        # for testing purposes
        parents = self.select_parents()


    def test_selection(self):
        c = self.roulette_wheel_selection()
        c.print_chromosome()


epoch = Epoch()
# epoch.test_selection()
epoch.print_epoch_info()