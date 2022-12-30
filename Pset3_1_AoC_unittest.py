import unittest

# AoC Pset 3

from Pset3_1_AoC import split_string

class TestString(unittest.TestCase):

    def test_split_string(self):
        # Setup
        string = "MVWpzTTrTFNNLtssjV"
        first_half, second_half = split_string(string)

        # Assert
        self.assertEqual(first_half, "MVWpzTTrT")
        self.assertEqual(second_half, "FNNLtssjV")


if __name__ == '__main__':
    unittest.main()