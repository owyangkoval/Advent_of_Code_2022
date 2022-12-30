# Rock Paper Scissors

def main():
    file = open('Pset2_1_AoC_input.txt', 'r')
    read = file.readlines()

    player_gameplay = Gameplay()
    for moves in read:
        player_gameplay.players_moves(moves[0], moves[2])
    print(f"Sums: P2 = {player_gameplay.player_2_sum()}")

class Gameplay:

    def __init__(self):
        self._player_2_score = []

    def get_player_1_score(self):
        return self._player_1_score

    def get_player_2_score(self):
        return self._player_2_score

    def players_moves(self, player_1_move, end_move):
        # Determine the points needed to add up the win/lose and choice score
        if player_1_move == "A" and end_move == "X":
            self._player_2_score.append(3+0)
        if player_1_move == "A" and end_move == "Y":
            self._player_2_score.append(1+3)
        if player_1_move == "A" and end_move == "Z":
            self._player_2_score.append(2+6)
        if player_1_move == "B" and end_move == "X":
            self._player_2_score.append(1+0)
        if player_1_move == "B" and end_move == "Y":
            self._player_2_score.append(2+3)
        if player_1_move == "B" and end_move == "Z":
            self._player_2_score.append(3+6)
        if player_1_move == "C" and end_move == "X":
            self._player_2_score.append(2+0)
        if player_1_move == "C" and end_move == "Y":
            self._player_2_score.append(3+3)
        if player_1_move == "C" and end_move == "Z":
            self._player_2_score.append(1+6)

    def player_2_sum(self):
        player_2_sum = 0
        for value in self._player_2_score:
            player_2_sum += value
        return player_2_sum



if __name__ == '__main__':
    main()
