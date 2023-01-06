import unittest

# AoC Pset 3

from Pset3_1_AoC import priorities_list

class TestString(unittest.TestCase):

    def test_priorities_list(self):
        # Setup
        string = "MVWpzTTrTFNNLtssjV"
        first_half, second_half, priority_list = priorities_list(string)

        # Assert
        self.assertEqual(first_half, ['M', 'V', 'W', 'p', 'z', 'T', 'T', 'r', 'T'])
        self.assertEqual(second_half, ['F', 'N', 'N', 'L', 't', 's', 's', 'j', 'V'])
        self.assertEqual(priority_list, [48])

if __name__ == '__main__':
    unittest.main()