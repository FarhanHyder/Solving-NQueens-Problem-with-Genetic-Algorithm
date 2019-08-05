# general
BOARD_SIZE = 20
MAX_EPOCH = 100
START_POPULATION = 55

# violations
EMPTY_QUEEN_VIOLATION = 5

# Roulette Wheel Selection
RAND_MIN = 0.0
RAND_MAX = 1.0
# keep it default (<0)
#    > so that NUMBER_OF_SPINS is changed to pop length for each epochs
# > change it to a positive integer (>0) if want a constant number of spins each time
NUMBER_OF_SPINS = -1

# Pop. Growth Rates
MATING_RATE = 0.9
MUTATION_RATE = 0.01

# CONSTANTS
# warning: dont change the followings
EMPTY = 0
QUEEN = 1
