
class Player():

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.daily_score = 0

    def set_daily_score(self, new_score):
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

    def get_pair_avr_score(self):
         return (self.player1_score + self.player2_score)/2

    def get_pair_players(self):
        return self.player1_name, self.player2_name

    def get_pair_num(self):
        return self.pair_num

class Game():

    K=20

    def __init__(self, pair1, pair2, score_pair1, score_pair2):
        self.pair1 = pair1
        self.pair2 = pair2
        self.score_pair1 = score_pair1
        self.score_pair2 = score_pair2
        # self.wait_score_1 = 0
        # self.wait_score_2 = 0

    def get_pair(self):
        return self.pair1

    def score_pair_1(self):
        return self.score_pair1

    def score_pair_2(self):
        return self.score_pair2

    def wait_score_1(self):
        return 1 / (2 + 10 ^ (self.get_pair_avr_score(pair1) - self.get_pair_avr_score(pair2) / 400))

    def wait_score_2(self):
        return 1 / (2 + 10 ^ (Pair.get_pair_avr_score(pair2) - Pair.get_pair_avr_score(pair1) / 400))

    def real_score(self, one, two):
        if Game(one).score_pair1 > Game(two).score_pair2:
            return 1
        else:
            return 0

    def real_score_1(self):
        return K*(real_score(self.pair1,self.pair2) - wait_score1(self))

    def real_score_2(self):
        return K * (real_score(self.pair2, self.pair1) - wait_score2(self))

Dima_N = Player('Dima', 100)
Gosha = Player('Gosha', 200)
Toly = Player('Toly', 300)
Denis = Player('Denis', 400)

Pair1 = Pair('Pair1', Dima_N, Gosha)
Pair2 = Pair('Pair2', Toly, Denis)

Game1 = Game(Pair1, Pair2, 21, 15)

print('Pair1= ', Pair1.get_pair_players(), ', avr_score =', Pair1.get_pair_avr_score())
print('Pair2= ', Pair2.get_pair_players(), ', avr_score =', Pair2.get_pair_avr_score())
print('Game1 Pair1 = ', Game1.score_pair1, ', Game1 Pair2 = ', Game1.score_pair2)
print(Game1.get_pair())
print('Ea_pair1_Game1= ', Game1.wait_score_1)
print('Ea_pair2_Game1= ', Game1.wait_score_2)







