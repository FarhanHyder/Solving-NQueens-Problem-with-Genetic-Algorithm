from unittest import TestCase
from NQueens import *

nq = NQueens()
chromosome = nq.create_empty_board()


class TestNQueens(TestCase):

    # pre: BOARD_SIZE must be at least 1
    def test_place_queen(self):
        # place a queen in 00
        nq.place_queen(chromosome, 0, 0)
        self.assertEqual(chromosome[0][0], QUEEN, "Queen placed successfully in 00")

    # pre: place_queen passes the test, BOARD_SIZE must be at least 3
    def test_remove_queen(self):
        nq.place_queen(chromosome, 0, 2)
        nq.remove_queen(chromosome, 0, 2)
        self.assertEqual(chromosome[0][2], EMPTY, "Queen successfully removed from 02")

    def test_create_empty_board(self):
        from math import sqrt
        chromosome = nq.create_empty_board()
        cond1 = (chromosome[0].size == int(sqrt(chromosome.size)))
        cond2 = (chromosome.size == (BOARD_SIZE * BOARD_SIZE))
        self.assertTrue(cond1 and cond2)

    # supplementary functions for test_check_n_violations
    def set_perfect_4_by_4_chromosome(self, chromo):
        nq.place_queen(chromo, 0, 2)
        nq.place_queen(chromo, 1, 0)
        nq.place_queen(chromo, 2, 3)
        nq.place_queen(chromo, 3, 1)

    def set_faulty_4_by_4_chromosome(self, chromo):
        nq.place_queen(chromo, 0, 0)
        nq.place_queen(chromo, 1, 1)
        nq.place_queen(chromo, 2, 2)
        nq.place_queen(chromo, 3, 3)

    # pre: place_queen passes the test
    def test_check_n_violations(self):
        SIZE = 4
        chromo = nq.create_empty_board(SIZE)
        self.set_perfect_4_by_4_chromosome(chromo)  # this version of ch does not have any violations
        cond1 = (nq.check_n_violations(chromo, 3, 1, SIZE=4) == 0)

        # let's give a super faulty one now
        chromo2 = nq.create_empty_board(SIZE)
        self.set_faulty_4_by_4_chromosome(chromo2)
        cond2 = (nq.check_n_violations(chromo2, 3, 3, SIZE=4) == 3)

        self.assertTrue(cond1 and cond2)

    # pre: BOARD_SIZE must be at least 2
    def test_get_queen_col_index(self):
        # chromosome is empty by default in this setup, so should return -1
        cond1 = (nq.get_queen_col_index(chromosome, 0) == -1)

        # let's place a queen in the second row
        nq.place_queen(chromosome, 1, 1)
        cond2 = (nq.get_queen_col_index(chromosome, 1) == 1)

        self.assertTrue(cond1 and cond2)

    def test_get_fitness(self):
        SIZE = 4
        chromo = nq.create_empty_board(SIZE)
        self.set_perfect_4_by_4_chromosome(chromo)  # this version of ch does not have any violations

        self.assertEqual(nq.get_fitness(chromo,SIZE=4),100)


