from unittest import TestCase
from NQueens import *

nq = NQueens()
board = nq.create_empty_board()
# nq.place_queen(board,0,2)
# nq.place_queen(board,1,0)
# nq.place_queen(board,2,3)
# nq.place_queen(board,3,1)


class TestNQueens(TestCase):
    def test_place_queen(self):
        # place a queen in 00
        nq.place_queen(board, 0, 0)
        self.assertEqual(board[0][0], QUEEN, "Queen placed successfully in 00")

    # pre: place_queen passes the test
    def test_remove_queen(self):
        nq.place_queen(board,0,2)
        nq.remove_queen(board,0,2)
        self.assertEqual(board[0][2], EMPTY, "Queen successfully removed from 02")




