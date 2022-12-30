import unittest

# AoC Pset 1

from Pset1_AoC import Elf, Calories

class TestElf(unittest.TestCase):

    def test_get_calories(self):
        # Setup
        first_elf = Elf([1000,2000,3000])
        second_elf = Elf([4000])
        third_elf = Elf([5000,6000])
        fourth_elf = Elf([7000,8000,9000])
        fifth_elf = Elf([10000])

        # Assert
        self.assertEqual(first_elf.get_calories(), [1000,2000,3000])
        self.assertEqual(second_elf.get_calories(), [4000])
        self.assertEqual(third_elf.get_calories(), [5000,6000])
        self.assertEqual(fourth_elf.get_calories(), [7000,8000,9000])
        self.assertEqual(fifth_elf.get_calories(), [10000])

    def test_get_calorie_sum(self):
        # Setup
        first_elf = Elf([1000,2000,3000])
        second_elf = Elf([4000])
        third_elf = Elf([5000,6000])
        fourth_elf = Elf([7000,8000,9000])
        fifth_elf = Elf([10000])

        # Assert
        self.assertEqual(first_elf.get_calorie_sum(), 6000)
        self.assertEqual(second_elf.get_calorie_sum(), 4000)
        self.assertEqual(third_elf.get_calorie_sum(), 11000)
        self.assertEqual(fourth_elf.get_calorie_sum(), 24000)
        self.assertEqual(fifth_elf.get_calorie_sum(), 10000)


class TestCalories(unittest.TestCase):

    def test_get_max_calories(self):
        # Setup
        first_elf = Elf([1000,2000,3000])
        second_elf = Elf([4000])
        third_elf = Elf([5000,6000])
        fourth_elf = Elf([7000,8000,9000])
        fifth_elf = Elf([10000])
        calories = Calories()
        calories.add_elf(first_elf)
        calories.add_elf(second_elf)
        calories.add_elf(third_elf)
        calories.add_elf(fourth_elf)
        calories.add_elf(fifth_elf)

        # Assert
        self.assertEqual(calories.get_max_calories(), 24000)



# AoC Pset 2


from Pset2_AoC import Gameplay


class TestGameplay(unittest.TestCase):

    def test_get_player_1_score(self):
        # Setup
        player_gameplay = Gameplay()
        player_gameplay.players_moves("A", "Y")
        player_gameplay.players_moves("B", "X")
        player_gameplay.players_moves("C", "Z")

        # Assert
        self.assertEqual(player_gameplay.get_player_1_score(), [1,0,2,6,3,3])
        self.assertEqual(player_gameplay.get_player_2_score(), [2,6,1,0,3,3])

    def test_player_1_sum(self):
        # Setup
        player_gameplay = Gameplay()
        player_gameplay.players_moves("A", "Y")
        player_gameplay.players_moves("B", "X")
        player_gameplay.players_moves("C", "Z")

        # Assert
        self.assertEqual(player_gameplay.player_1_sum(), 15)

    def test_player_2_sum(self):
        # Setup
        player_gameplay = Gameplay()
        player_gameplay.players_moves("A", "Y")
        player_gameplay.players_moves("B", "X")
        player_gameplay.players_moves("C", "Z")

        # Assert
        self.assertEqual(player_gameplay.player_1_sum(), 15)

if __name__ == '__main__':
    unittest.main()