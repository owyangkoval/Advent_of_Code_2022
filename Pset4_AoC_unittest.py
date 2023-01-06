import unittest

from Pset4_1_AoC import SectionIDs

class TestSectionIDs(unittest.TestCase):

    def test_check_overlap(self):
        # Setup
        section_ids = SectionIDs()
        string = "2-4,6-8"

        # Assert
        self.assertEqual(section_ids.check_overlap(string), 0)

if __name__ == '__main__':
    unittest.main()