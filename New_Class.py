import DB_SQLite


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
        self.players = [player1, player2, player3, player4]
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
            if i['name'] == self.players[0].name:
                i['daily_score'] = self.players[0].daily_score
            elif i['name'] == self.players[1].name:
                i['daily_score'] = self.players[1].daily_score
            elif i['name'] == self.players[2].name:
                i['daily_score'] = self.players[2].daily_score
            elif i['name'] == self.players[3].name:
                i['daily_score'] = self.players[3].daily_score

    def extend_players_dict(self, dict):
        #  added all new players (name and current score) of current Game to argument list
        #  This method should execute after Day, not after each Game.
        dict.extend(self.Temp_Players_Dict)

    def list_daily_new_player(self, temp_dict):
        #  List players what not exist in previous games statistics
        if len(self.Temp_Players_Dict) != 0:
            for i in self.Temp_Players_Dict:
                 temp_dict.append(i['name'])
            return temp_dict
        else:
            pass
    @staticmethod
    def print_list_new_player(date, temp_dict):
        if len(temp_dict) != 0:
            print(f'+     В этой день ({date}) у нас новый(вые) игрок(и) - ', ", ".join(temp_dict))
        else:
            pass

    def create_temp_players(self):
        #  Code will check if Players from external file.
        #  For exist Player - create score from list. If Player not exist in file = new Player - create default score '500'
        #  List of Game Players will keep in Online_Players_Dict
        #  If Player not exist in external file -> add this Player to Temp_Players_Dict
        for player, i in zip(self.players, (0, 1, 2, 3)):
            if not isinstance(self.players[i], Player):
                for ii in self.Temp_import_players:
                    if ii['name'] == self.players[i]:
                        self.players[i] = Player(self.players[i], ii['score'], ii['daily_score'])
                        a = dict(name=self.players[i].name, score=self.players[i].score, daily_score=self.players[i].daily_score)
                        self.Online_Players_Dict.append(a)
                if not isinstance(self.players[i], Player):
                    self.players[i] = Player(self.players[i])
                    a = dict(name=self.players[i].name, score=self.players[i].score, daily_score=self.players[i].daily_score)
                    self.Online_Players_Dict.append(a)
                    self.Temp_Players_Dict.append(a)


    def get_pair_avr_score(self, pl_1, pl_2):
        #  Count average score of the pairs by formula (score1+score2)/2
        return (pl_1.score + pl_2.score) / 2


    def wait_score_2(self):
        #  Found waiting score of the Pair1 in game by Elo formula.
        return 1 / (1 + 10 ** ((
                self.get_pair_avr_score(self.players[0], self.players[1]) - self.get_pair_avr_score(self.players[2],
                                                                                              self.players[3])) / 100))

    def wait_score_1(self):
        #  Found waiting score of the Pair2 in game by Elo formula.
        return 1 / (1 + 10 ** ((
                self.get_pair_avr_score(self.players[2], self.players[3]) - self.get_pair_avr_score(self.players[0],
                                                                                              self.players[1])) / 100))

    @staticmethod
    def real_score(one, two):
        # compare Game score between Pairs and found parameter of the winners (if win = 1, if loose = 0, for 21:23
        # need add 0.2 and update logic later)
        if 10 >= two < one >= 21:  #  Побелили через 10
            return 1.2
        elif 10 >= one < two:      #  Проиграли через 10
            return -0.2
        elif 20 > one < two:       #  Проиграли обычно
            return 0
        elif 20 <= one < two:      #  Проиграли на балансе
            return 0.2
        elif one > two >= 20:      #  Выйграли на балансе
            return 0.8
        elif 10 < two < one >= 21: #  Выйграли обычно
            return 1


    def real_score_1(self):
        #  found update Pair1 score what will be used to multiply with Player daily score. 20 - need update later
        return 20 * (self.real_score(self.score_pair1, self.score_pair2) - self.wait_score_1())

    def real_score_2(self):
        #  found update Pair2 score what will be used to multiply with Player daily score. 20 - need update later
        return 20 * (self.real_score(self.score_pair2, self.score_pair1) - self.wait_score_2())

    @staticmethod
    def win_lose_max_min(score1, score2):
        temp = [0, 0, 0]
        if score1 > score2:  # Who win = 1, who lose = 0
            temp[0] = 1
        if score1 > 21 or score2 > 21:  # if game on balance
            temp[1] = 1
        if score1 <= 10 or score2 <= 10:  # if game more than 10 score
            temp[2] = 1
        return temp

    def set_daily_score(self, date):
        #  this method updated daily score for each Player in this Game.
        self.date = date
        self.players[0].set_daily_score(self.real_score_1())
        self.players[1].set_daily_score(self.real_score_1())
        self.players[2].set_daily_score(self.real_score_2())
        self.players[3].set_daily_score(self.real_score_2())
        self.insert_user_data_to_DB(date)
        # return print('game=', self.date,'\n',self.players[0].name, '=', self.players[0].daily_score,'current=',self.players[0].score,'\n',
        #              self.players[1].name, '=', self.players[1].daily_score,'current=',self.players[1].score,'\n',
        #              '  score=',self.score_pair1,'pair_avr=',self.get_pair_avr_score(self.players[0], self.players[1]),'Ea=',self.wait_score_1(),'Sa=',self.real_score(self.score_pair1, self.score_pair2),'Ra=',self.real_score_1(),'\n',
        #              self.players[2].name, '=', self.players[2].daily_score,'current=',self.players[2].score,'\n',
        #              self.players[3].name, '=', self.players[3].daily_score,'current=',self.players[3].score,'\n',
        #              '  score=',self.score_pair2,'pair_avr=',self.get_pair_avr_score(self.players[2], self.players[3]),'Ea=',self.wait_score_2(),'Sa=',self.real_score(self.score_pair2, self.score_pair1),'Ra=',self.real_score_2())

    def insert_user_data_to_DB(self, date):
        self.date = date
        stat = (self.date,
                self.players[0].name, self.players[0].daily_score, self.players[0].score,
                self.players[1].name, self.players[1].daily_score, self.players[1].score,
                self.score_pair1,
                self.win_lose_max_min(self.score_pair1, self.score_pair2)[0],
                self.win_lose_max_min(self.score_pair1, self.score_pair2)[1],
                self.win_lose_max_min(self.score_pair1, self.score_pair2)[2],
                self.get_pair_avr_score(self.players[0], self.players[1]), self.wait_score_1(),
                self.real_score(self.score_pair1, self.score_pair2), self.real_score_1(),
                self.players[2].name, self.players[2].daily_score, self.players[2].score,
                self.players[3].name, self.players[3].daily_score, self.players[3].score,
                self.score_pair2,
                self.win_lose_max_min(self.score_pair2, self.score_pair1)[0],
                self.win_lose_max_min(self.score_pair2, self.score_pair1)[1],
                self.win_lose_max_min(self.score_pair2, self.score_pair1)[2],
                self.get_pair_avr_score(self.players[2], self.players[3]), self.wait_score_2(),
                self.real_score(self.score_pair2, self.score_pair1), self.real_score_2())
        DB_SQLite.insert_stat(stat)


    def update_players(self):
        #  this method call Player Class and update current Players score for all Players in this Game
        #  Should be called only 1 time in Day. NOT after each Game
        self.players[0].update_score()
        self.players[1].update_score()
        self.players[2].update_score()
        self.players[3].update_score()
        return print(self.players[0].name, '=', self.players[0].score,
                     self.players[1].name, '=', self.players[1].score,
                     self.players[2].name, '=', self.players[2].score,
                     self.players[3].name, '=', self.players[3].score)

    def update_player_score_in_dict(self, dict):
        #  Find all current Players from argument and update their personal score.
        #  This method should execute after current Day, NOT after each Game
        for i in dict:
            if i['name'] == self.players[0].name:
                i['score'] = self.players[0].score
            elif i['name'] == self.players[1].name:
                i['score'] = self.players[1].score
            elif i['name'] == self.players[2].name:
                i['score'] = self.players[2].score
            elif i['name'] == self.players[3].name:
                i['score'] = self.players[3].score

class Day:

    def __init__(self, date, games):
        self.date = date
        self.list_of_games = games

    def start_games_counting(self, Players_Dict):
        temp_dict = []
        for i in self.list_of_games:
            self.game = Game(i['player1'], i['player2'], i['player3'], i['player4'], i['score1'], i['score2'])
            self.game.import_players(Players_Dict)  # this is for each game
            self.game.create_temp_players()         # this is for each game
            self.game.set_daily_score(self.date)    # this is after each game
            self.game.list_daily_new_player(temp_dict)            # Сохраняю имена всех игроков которых нет в предыдущей статистике.
            self.game.extend_players_dict(Players_Dict)
            self.game.update_daily_score_in_dict(Players_Dict)
        self.game.print_list_new_player(self.date, temp_dict)  # Печатаю всех новых игроков за этот игровой день
        for i in Players_Dict:   # Update score in Players_Dict after each day of games. Mandatory.
            i['score'] = i['score'] + i['daily_score']
            i['daily_score'] = 0
            #print(f"{i['name']}={i['score']}")
        count_games = DB_SQLite.count_games_in_day_from_db(self.date)
        print(f'  В этот игровой день ({self.date}) было ({count_games[0]}) игр.')
        #print(f'В этот игровой день ({self.date}) было ({count_games[0]}) игр. Игроки: ', *(i['name'] for i in Players_Dict),',')
        #print(f'После игрового дня {self.date} статистика', *((i['name'], int(i['score'])) for i in Players_Dict))
        print()
