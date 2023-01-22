class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.daily_score = 0

    def set_daily_score(self, new_score):
        #  update player daily score after each game
        self.daily_score = self.daily_score + new_score
        return self.get_daily_score()

    def get_daily_score(self):
        return self.daily_score

    def get_score(self):
        return self.score

    def update_score(self):
        self.score = self.score + self.daily_score
        return self.score

    def name(self):
        return self.name

class Pair(Player):

    def __init__(self, pair_num, player1, player2):
        self.pair_num = pair_num
        self.player1 = player1
        self.player2 = player2

    def get_pair_avr_score(self):
        #  found average pair score for next estimation
        return (self.player1.score + self.player2.score)/2

    def get_pair_players(self):
        return self.player1.name, self.player2.name

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
        return 1 / (2 + 10 ** (self.pair1.get_pair_avr_score(,, - self.pair2.get_pair_avr_score(,,) / 400)

    def wait_score_2(self):
        #  Found waiting score of the Pair2 in game by Elo formula.
        return 1 / (2 + 10 ** (self.pair2.get_pair_avr_score(,, - self.pair1.get_pair_avr_score(,,) / 400)

    def real_score(self, one, two):
        # compare Game score between Pairs and found parameter of the winners (if win = 1, if loose = 0, for 21:23
        # need add 0.2 and update logic later)
        if one > two and one >= 21:
            return 1
        elif two > one and one < 20:
            return 0
        elif two > one and one >= 20:
            return 0.2

    def real_score_1(self):
        #  found update Pair1 score what will be used to multiply with Player daily score. 20 - need update later
        return 20 * (self.real_score(self.score_pair1, self.score_pair2) - self.wait_score_1())

    def real_score_2(self):
        #  found update Pair2 score what will be used to multiply with Player daily score. 20 - need update later
        return 20 * (self.real_score(self.score_pair2, self.score_pair1) - self.wait_score_2())

    def update_players(self):
        #  this method updated daily score for each Player in this Game.
        self.pair1.player1.set_daily_score(self.real_score_1())
        self.pair1.player2.set_daily_score(self.real_score_1())
        self.pair2.player1.set_daily_score(self.real_score_2())
        self.pair2.player2.set_daily_score(self.real_score_2())
        #return print(Dima.get_daily_score(),Gosha.get_daily_score(),Toly.get_daily_score(),Denis.get_daily_score())

class Day(Game):

    def __init__(self, date, day_games):
        self.date = date
        self.day_games = day_games

    def update_day_score(self):
        for i in range(len(self.day_games)):
            self.day_games[i].update_players()

    def get_day(self):
        return self.date