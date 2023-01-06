# Rock Paper Scissors

def main():
    file = open('Pset2_AoC_input.txt', 'r')
    read = file.readlines()

    player_gameplay = Gameplay()
    for moves in read:
        player_gameplay.players_moves(moves[0], moves[2])
    print(f"Sums: P1 = {player_gameplay.player_1_sum()}, P2 = {player_gameplay.player_2_sum()}")

class Gameplay:

    def __init__(self):
        self._player_1_score = []
        self._player_2_score = []

    def get_player_1_score(self):
        return self._player_1_score

    def get_player_2_score(self):
        return self._player_2_score

    def players_moves(self, player_1_move, player_2_move):
        # Determine the points needed to add up the win/lose and choice score
        if player_1_move == "A" and player_2_move == "X":
            self._player_1_score.append(3+1)
            self._player_2_score.append(3+1)
        if player_1_move == "A" and player_2_move == "Y":
            self._player_1_score.append(0+1)
            self._player_2_score.append(6+2)
        if player_1_move == "A" and player_2_move == "Z":
            self._player_1_score.append(6+1)
            self._player_2_score.append(0+3)
        if player_1_move == "B" and player_2_move == "X":
            self._player_1_score.append(6+2)
            self._player_2_score.append(0+1)
        if player_1_move == "B" and player_2_move == "Y":
            self._player_1_score.append(3+2)
            self._player_2_score.append(3+2)
        if player_1_move == "B" and player_2_move == "Z":
            self._player_1_score.append(0+2)
            self._player_2_score.append(6+3)
        if player_1_move == "C" and player_2_move == "X":
            self._player_1_score.append(0+3)
            self._player_2_score.append(6+1)
        if player_1_move == "C" and player_2_move == "Y":
            self._player_1_score.append(6+3)
            self._player_2_score.append(0+2)
        if player_1_move == "C" and player_2_move == "Z":
            self._player_1_score.append(3+3)
            self._player_2_score.append(3+3)

    def player_1_sum(self):
        player_1_sum = 0
        for value in self._player_1_score:
            player_1_sum += value
        return player_1_sum

    def player_2_sum(self):
        player_2_sum = 0
        for value in self._player_2_score:
            player_2_sum += value
        return player_2_sum


if __name__ == '__main__':
    main()