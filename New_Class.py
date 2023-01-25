class Player:

    def __init__(self, name, score=500, daily_score=0):
        self.name = name
        self.score = score
        self.daily_score = daily_score

    def set_daily_score(self, new_score):
        #  update player daily score after each game
        self.daily_score = self.daily_score + new_score
        return self.get_daily_score()

    def get_daily_score(self):
        return self.daily_score

    def get_score(self):
        return self.score

    def update_score(self):
        #  update personal score after each day
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
        self.Online_Players_Dict = []
        self.Temp_Players_Dict = []
        self.Temp_import_players = []

    def import_players(self, dict):
        #  import all previous players with score to current game. Each game need to execute.
        #  Using by create_temp_players def
        self.Temp_import_players = dict

    def update_daily_score_in_dict(self, dict):
        for i in dict:
            if i['name'] == self.player1.name:
                i['daily_score'] = self.player1.daily_score
            elif i['name'] == self.player2.name:
                i['daily_score'] = self.player2.daily_score
            elif i['name'] == self.player3.name:
                i['daily_score'] = self.player3.daily_score
            elif i['name'] == self.player4.name:
                i['daily_score'] = self.player4.daily_score

    def extend_players_dict(self, dict):
        #  added all new players (name and current score) of current Game to argement list
        #  This method should execute after Day, not after each Game.
        dict.extend(self.Temp_Players_Dict)


    def create_temp_players(self):
        #  Code will check if Players from external file.
        #  For exist Player - create score from list, for new Player - create default score '500'
        #  List of Game Players will keep in Online_Players_Dict
        #  If Player not exist in external file -> add this Player to Temp_Players_Dict
        for i in 1, 2, 3, 4:
            temp = self.__getattribute__('player%d' % i)
            if not isinstance(temp, Player):
                for ii in self.Temp_import_players:
                    if ii['name'] == self.__getattribute__('player%d' % i):
                        self.__setattr__('player%d' % i, Player(self.__getattribute__('player%d' % i), ii['score'], ii['daily_score']))
                        b = self.__getattribute__('player%d' % i)
                        a = dict(name=b.name, score=b.score, daily_score=b.daily_score)
                        self.Online_Players_Dict.append(a)
                temp = self.__getattribute__('player%d' % i)
                if not isinstance(temp, Player):
                    self.__setattr__('player%d' % i, Player(self.__getattribute__('player%d' % i)))
                    b = self.__getattribute__('player%d' %i)
                    a = dict(name=b.name, score=b.score, daily_score=b.daily_score)
                    self.Online_Players_Dict.append(a)
                    self.Temp_Players_Dict.append(a)


    def get_pair_avr_score(self, pl_1, pl_2):
        #  Count average score of the pairs by formula (score1+score2)/2
        return (pl_1.score + pl_2.score) / 2


    def wait_score_2(self):
        #  Found waiting score of the Pair1 in game by Elo formula.
        return 1 / (1 + 10 ** ((
                self.get_pair_avr_score(self.player1, self.player2) - self.get_pair_avr_score(self.player3,
                                                                                              self.player4)) / 100))

    def wait_score_1(self):
        #  Found waiting score of the Pair2 in game by Elo formula.
        return 1 / (1 + 10 ** ((
                self.get_pair_avr_score(self.player3, self.player4) - self.get_pair_avr_score(self.player1,
                                                                                              self.player2)) / 100))

    def real_score(self, one, two):
        # compare Game score between Pairs and found parameter of the winners (if win = 1, if loose = 0, for 21:23
        # need add 0.2 and update logic later)
        if 21 <= one > two:
            return 1
        elif two > one < 20:
            return 0
        elif two > one >= 20:
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
        return print('game \n',self.player1.name, '=', self.player1.daily_score,'current=',self.player1.score,'\n',
                     self.player2.name, '=', self.player2.daily_score,'current=',self.player2.score,'\n',
                     '  score=',self.score_pair1,'pair_avr=',self.get_pair_avr_score(self.player1, self.player2),'Ea=',self.wait_score_1(),'Sa=',self.real_score(self.score_pair1, self.score_pair2),'Ra=',self.real_score_1(),'\n',
                     self.player3.name, '=', self.player3.daily_score,'current=',self.player3.score,'\n',
                     self.player4.name, '=', self.player4.daily_score,'current=',self.player4.score,'\n',
                     '  score=',self.score_pair2,'pair_avr=',self.get_pair_avr_score(self.player3, self.player4),'Ea=',self.wait_score_2(),'Sa=',self.real_score(self.score_pair2, self.score_pair1),'Ra=',self.real_score_2())

    def update_players(self):
        #  this method call Player Class and update current Players score for all Players in this Game
        #  Should be called only 1 time in Day. NOT after each Game
        self.player1.update_score()
        self.player2.update_score()
        self.player3.update_score()
        self.player4.update_score()
        return print(self.player1.name, '=', self.player1.score,
                     self.player2.name, '=', self.player2.score,
                     self.player3.name, '=', self.player3.score,
                     self.player4.name, '=', self.player4.score)

    def update_player_score_in_dict(self, dict):
        #  Find all current Players from argument and update their personal score.
        #  This method should execute after current Day, NOT after each Game
        for i in dict:
            if i['name'] == self.player1.name:
                i['score'] = self.player1.score
            elif i['name'] == self.player2.name:
                i['score'] = self.player2.score
            elif i['name'] == self.player3.name:
                i['score'] = self.player3.score
            elif i['name'] == self.player4.name:
                i['score'] = self.player4.score

class Day:

    def __init__(self, day, games):
        self.day = day
        self.list_of_games = games

    def start_games_counting(self, Players_Dict):
        for i in self.list_of_games:
            self.game = Game(i['player1'], i['player2'], i['player3'], i['player4'], i['score1'], i['score2'])
            self.game.import_players(Players_Dict)  # this is for each game
            self.game.create_temp_players()  # this is for each game
            self.game.set_daily_score()  # this is after each game
            self.game.extend_players_dict(Players_Dict)
            self.game.update_daily_score_in_dict(Players_Dict)
        for i in Players_Dict:
            i['score'] = i['score'] + i['daily_score']
            i['daily_score'] = 0
        print('After full Day', Players_Dict)