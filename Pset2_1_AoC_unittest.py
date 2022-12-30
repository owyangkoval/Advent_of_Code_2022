import unittest

# AoC Pset 2


from Pset2_1_AoC import Gameplay


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