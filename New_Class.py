class Player:

    def __init__(self, name, score=500):
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


class Game:

    def __init__(self, player1, player2, player3, player4, score_pair1, score_pair2):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.score_pair1 = score_pair1
        self.score_pair2 = score_pair2
        self.Online_Players_Dict =[]
        self.Temp_Players_Dict = []

    def new(self):
        if not isinstance(self.player1, Player):
            for i in Players_Dict:
                 if i['name'] == self.player1:
                      self.player1 = Player(self.player1, i['score'])
                      a = dict(name=self.player1.name, score=self.player1.score)
                      self.Online_Players_Dict.append(a)
            if not isinstance(self.player1, Player):
                self.player1 = Player(self.player1)
                a = dict(name=self.player1.name, score=self.player1.score)
                self.Online_Players_Dict.append(a)
                self.Temp_Players_Dict.append(a)

        if not isinstance(self.player2, Player):
            for i in Players_Dict:
                if i['name'] == self.player2:
                    self.player2 = Player(self.player2, i['score'])
                    a = dict(name=self.player2.name, score=self.player2.score)
                    self.Online_Players_Dict.append(a)
            if not isinstance(self.player2, Player):
                self.player2 = Player(self.player2)
                a = dict(name=self.player2.name, score=self.player2.score)
                self.Online_Players_Dict.append(a)
                self.Temp_Players_Dict.append(a)

        if not isinstance(self.player3, Player):
            for i in Players_Dict:
                if i['name'] == self.player3:
                    self.player3 = Player(self.player3, i['score'])
                    a = dict(name=self.player3.name, score=self.player3.score)
                    self.Online_Players_Dict.append(a)
            if not isinstance(self.player3, Player):
                self.player3 = Player(self.player3)
                a = dict(name=self.player3.name, score=self.player3.score)
                self.Online_Players_Dict.append(a)
                self.Temp_Players_Dict.append(a)

        if not isinstance(self.player4, Player):
            for i in Players_Dict:
                if i['name'] == self.player4:
                    self.player4 = Player(self.player4, i['score'])
                    a = dict(name=self.player4.name, score=self.player4.score)
                    self.Online_Players_Dict.append(a)
            if not isinstance(self.player4, Player):
                self.player4 = Player(self.player4)
                a = dict(name=self.player4.name, score=self.player4.score)
                self.Online_Players_Dict.append(a)
                self.Temp_Players_Dict.append(a)

        Players_Dict.extend(self.Temp_Players_Dict)

    def get_pair_avr_score(self, pl_1, pl_2):
        #  Count average score of the pairs by formula (score1+score2)/2
        return (pl_1.score + pl_2.score) / 2

    def score_pair_1(self):
        return self.score_pair1

    def score_pair_2(self):
        return self.score_pair2

    def wait_score_1(self):
        #  Found waiting score of the Pair1 in game by Elo formula.
        return 1 / (2 + 10 ** (
                self.get_pair_avr_score(self.player1, self.player2) - self.get_pair_avr_score(self.player3,
                                                                                              self.player4)) / 400)

    def wait_score_2(self):
        #  Found waiting score of the Pair2 in game by Elo formula.
        return 1 / (2 + 10 ** (
                self.get_pair_avr_score(self.player3, self.player4) - self.get_pair_avr_score(self.player1,
                                                                                              self.player2)) / 400)

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

    def set_daily_score(self):
        #  this method updated daily score for each Player in this Game.
        self.player1.set_daily_score(self.real_score_1())
        self.player2.set_daily_score(self.real_score_1())
        self.player3.set_daily_score(self.real_score_2())
        self.player4.set_daily_score(self.real_score_2())

    def update_players(self):
        self.player1.update_score()
        self.player2.update_score()
        self.player3.update_score()
        self.player4.update_score()
        return print(self.player1.name, '=', self.player1.score,
                     self.player2.name, '=', self.player2.score,
                     self.player3.name, '=', self.player3.score,
                     self.player4.name, '=', self.player4.score)

    def update_pl_dict(self):
        for i in Players_Dict:
            if i['name'] == self.player1.name:
                i['score'] = self.player1.score
            elif i['name'] == self.player2.name:
                i['score'] = self.player2.score
            elif i['name'] == self.player3.name:
                i['score'] = self.player3.score
            elif i['name'] == self.player4.name:
                i['score'] = self.player4.score
