import unittest
from game2 import Tic_Tac_Toe


class TestGame(unittest.TestCase):

    def setUp(self):
        self.t = Tic_Tac_Toe()

    def test_check(self):
        self.t.move = 4
        self.t.board = ['X', 'X', 'X', 'O', 'O', 6, 7, 8, 9]
        self.assertEqual(self.t.check(), 1)
        self.t.board = [1, 'O', 3, 'X', 'X', 'X', 7, 'O', 9]
        self.assertEqual(self.t.check(), 1)
        self.t.board = [1, 2, 3, 'O', 'O', 6, 'X', 'X', 'X']
        self.assertEqual(self.t.check(), 1)
        self.t.board = ['O', 'O', 'O', 'X', 'X', 6, 7, 8, 9]
        self.assertEqual(self.t.check(), 2)
        self.t.board = ['X', 'O', 'X', 'X', 'O', 6, 'X', 8, 9]
        self.assertEqual(self.t.check(), 1)
        self.t.board = [1, 'O', 'X', 'X', 'O', 'X', 7, 'O', 9]
        self.assertEqual(self.t.check(), 2)
        self.t.board = [1, 'O', 'X', 4, 'O', 'X', 7, 9, 'X']
        self.assertEqual(self.t.check(), 1)
        self.t.board = ['X', 'O', 3, 'O', 'X', 6, 7, 8, 'X']
        self.assertEqual(self.t.check(), 1)
        self.t.board = ['O', 'O', 'X', 4, 'X', 6, 'X', 8, 9]
        self.assertEqual(self.t.check(), 1)
        self.t.board = ['O', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'X']
        self.assertEqual(self.t.check(), 0)

    def test_check_input(self):
        self.assertEqual(self.t.check_input('3'), 0)
        self.assertEqual(self.t.check_input('1'), 0)
        self.assertEqual(self.t.check_input('-1'), 1)
        self.assertEqual(self.t.check_input('55'), 1)
        self.assertEqual(self.t.check_input('str'), 1)
        self.t.board = ['O', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'X']
        self.assertEqual(self.t.check_input('1'), 2)


if __name__ == '__main__':
    unittest.main()
