from decimal import Decimal


class Player():

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.daily_score = 0

    def set_daily_score(self, new_score):
        #  update player daily score after each game
        self.daily_score = self.daily_score + new_score

    def get_daily_score(self):
        return self.daily_score

    def get_score(self):
        return self.score

    def name(self):
        return self.name

class Pair(Player):

    def __init__(self, pair_num, player1, player2):
        self.pair_num = pair_num
        self.player1_name = Player.name(player1)
        self.player2_name = Player.name(player2)
        self.player1_score = Player.get_score(player1)
        self.player2_score = Player.get_score(player2)
        self.player1_daily_score = Player.get_daily_score(player1)
        self.player2_daily_score = Player.get_daily_score(player2)

    def get_pair_avr_score(self):
        #  found average pair score for next estimation
        return (self.player1_score + self.player2_score)/2

    def get_pair_players(self):
        return self.player1_name, self.player2_name

    def get_pair_num(self):
        return self.pair_num

class Game(Pair):

    def __init__(self, pair1, pair2, score_pair1, score_pair2):
        self.pair1 = pair1
        self.pair2 = pair2
        self.score_pair1 = score_pair1
        self.score_pair2 = score_pair2

    def get_pair(self):
        return self.pair1.pair_num, self.pair2.pair_num

    def score_pair_1(self):
        return self.score_pair1

    def score_pair_2(self):
        return self.score_pair2

    def wait_score_1(self):
        #  Found waiting score of the Pair1 in game by Elo formula.
        return 1 / (2 + 10 ** (self.pair1.get_pair_avr_score() - self.pair2.get_pair_avr_score()) / 400)

    def wait_score_2(self):
        #  Found waiting score of the Pair2 in game by Elo formula.
        return 1 / (2 + 10 ** (self.pair2.get_pair_avr_score() - self.pair1.get_pair_avr_score()) / 400)

    def real_score(self, one, two):
        # compare Game score between Pairs and found parameter of the winners (if win = 1, if loose = 0, for 21:21 need add 0.5)
        if one > two:
            return 1
        else:
            return 0

    def real_score_1(self):
        #  found update Pair1 score what will be used to multiply with Player daily score. 20 - need update later
        return 20 * (self.real_score(self.score_pair1, self.score_pair2) - self.wait_score_1())

    def real_score_2(self):
        #  found update Pair2 score what will be used to multiply with Player daily score. 20 - need update later
        return 20 * (self.real_score(self.score_pair2, self.score_pair1) - self.wait_score_2())

    def get_sc(self):
        return self.pair1.player1_name(get_daily_score)


Dima = Player('Dima', 500)
Gosha = Player('Gosha', 500)
Toly = Player('Toly', 500)
Denis = Player('Denis', 500)

Pair1 = Pair('Pair1', Dima, Gosha)
Pair2 = Pair('Pair2', Toly, Denis)

Game1 = Game(Pair1, Pair2, 21, 15)

print('Pair1= ', Pair1.get_pair_players(), ', avr_score =', Pair1.get_pair_avr_score())
print('Pair2= ', Pair2.get_pair_players(), ', avr_score =', Pair2.get_pair_avr_score())
print('Game1 Pair1 = ', Game1.score_pair1, ', Game1 Pair2 = ', Game1.score_pair2)
print('Game1 Pair1/Pair2 = ',Game1.get_pair())
print('Ea_pair1_Game1= ', Game1.wait_score_1())
print('Ea_pair2_Game1= ', Game1.wait_score_2())
print('Real_Score_1 = ', Game1.real_score_1())
print('Real_Score_2 = ', Game1.real_score_2())
print('Daily_Score_Player1 = ', Game1.pair1.player1_name, Game1.pair1.pair_num, Pair1.player1_daily_score)
print(Game1.get_sc())







