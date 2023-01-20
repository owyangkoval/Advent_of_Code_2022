import unittest

from Pset5_1_AoC import move_block, print_matrix

class TestCase(unittest.TestCase):

    def test_find_from_top_block(self):
        # Setup
        matrix = [[' ', ' ', 'M'],
                  [' ', ' ', 'D'],
                  [' ', ' ', 'S'],
                  [' ', 'H', 'R']]
        move_block((1, 3), (2, 1), matrix)
        print_matrix(matrix)

        # Test
        self.assertEqual()

    def test_move_block(self):
        # Setup
        matrix = [[' ', ' ', 'M'],
                  ['V', ' ', 'D'],
                  ['L', ' ', 'S'],
                  ['D', 'H', 'R']]
        move_block((1, 0), (2, 1), matrix)
        print_matrix(matrix)

        # Test
        self.assertEqual(matrix, [[' ', ' ', 'M'], [' ', ' ', 'D'], ['L', 'V', 'S'],
                  ['D', 'H', 'R']])


if __name__ == '__main__':
    unittest.main()