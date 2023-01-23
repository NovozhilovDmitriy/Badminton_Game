from New_Class import Player, Game, Day

Players_Dict = []
#Players_Dict = [{'name': 'Дима Н', 'score': 500,'daily_score': 0}]

#print('Game1')
# print('Current player list in HDD', Players_Dict)
#game1 = Game('Коля', 'Дима Н', 'Женя', 'Антон Б', 21, 9)
# game2 = Game('Гоша', 'Толик', 'Миша', 'Макс', 21, 17)
# game3 = Game('Макс', 'Дима Н', 'Коля', 'Миша', 21, 19)
# game4 = Game('Ира',	'Гоша',	'Женя',	'Толик', 15, 21)
# game5 = Game('Антон Б',	'Гоша',	'Коля',	'Толик', 8, 21)
# game6 = Game('Женя', 'Миша', 'Макс', 'Ира', 21,	18)
# game7 = Game('Макс', 'Толик', 'Ира', 'Антон Б', 21,	10)
# game8 = Game('Миша', 'Дима Н', 'Коля', 'Женя', 18, 21)
# game9 = Game('Миша', 'Ира', 'Макс', 'Антон Б', 12, 21)
# game10 = Game('Коля', 'Гоша', 'Женя', 'Дима Н', 19, 21)
# game11 = Game('Антон Б', 'Гоша', 'Женя', 'Миша', 12, 21)
# game12 = Game('Дима Н',	'Толик', 'Макс', 'Ира',	21,12)
# game13 = Game('Ира', 'Толик', 'Коля', 'Миша', 14, 21)
# game14 = Game('Дима Н',	'Гоша', 'Макс', 'Антон Б', 19, 21)
# game15 = Game('Ира', 'Антон Б', 'Женя' , 'Дима Н', 15, 21)
# game16 = Game('Коля', 'Гоша', 'Макс', 'Толик', 21, 17)
# game17 = Game('Коля', 'Дима Н',	'Миша', 'Гоша', 21, 19)
# game18 = Game('Антон Б', 'Толик', 'Женя', 'Ира', 15, 21)
# game19 = Game('Коля', 'Женя', 'Макс', 'Гоша', 12, 21)
# game20 = Game('Антон Б', 'Дима Н', 'Миша', 'Толик', 16,	21)
# game21 = Game('Ира', 'Гоша', 'Миша', 'Дима Н', 11, 21)
# game22 = Game('Коля', 'Толик', 'Женя', 'Макс', 21, 14)

games = [{'player1': 'Коля', 'player2': 'Дима Н', 'player3': 'Женя', 'player4': 'Антон Б', 'score1': 21, 'score2': 9},
            {'player1': 'Гоша', 'player2': 'Толик', 'player3': 'Миша', 'player4': 'Макс','score1': 21, 'score2': 17},
            {'player1': 'Макс', 'player2': 'Дима Н', 'player3': 'Коля', 'player4':'Миша','score1': 21, 'score2': 19},
            {'player1': 'Ира', 'player2': 'Гоша', 'player3': 'Женя', 'player4':	'Толик','score1': 15, 'score2': 21},
            {'player1': 'Антон Б', 'player2': 'Гоша', 'player3': 'Коля', 'player4': 'Толик','score1': 8, 'score2': 21},
            {'player1': 'Женя', 'player2': 'Миша', 'player3': 'Макс', 'player4': 'Ира','score1': 21, 'score2':	18},
            {'player1': 'Макс', 'player2': 'Толик', 'player3': 'Ира', 'player4': 'Антон Б','score1': 21, 'score2':	10},
            {'player1': 'Миша', 'player2': 'Дима Н', 'player3': 'Коля', 'player4': 'Женя','score1': 18, 'score2': 21},
            {'player1': 'Миша', 'player2': 'Ира', 'player3': 'Макс', 'player4': 'Антон Б','score1': 12, 'score2': 21},
            {'player1': 'Коля', 'player2': 'Гоша', 'player3': 'Женя', 'player4': 'Дима Н','score1': 19,  'score2':21},
            {'player1': 'Антон Б', 'player2': 'Гоша', 'player3': 'Женя', 'player4': 'Миша','score1': 12, 'score2': 21},
            {'player1': 'Дима Н', 'player2': 'Толик', 'player3': 'Макс', 'player4': 'Ира','score1':	21, 'score2':12},
            {'player1': 'Ира', 'player2': 'Толик', 'player3': 'Коля', 'player4': 'Миша','score1': 14, 'score2': 21},
            {'player1': 'Дима Н', 'player2':	'Гоша', 'player3': 'Макс', 'player4': 'Антон Б','score1': 19, 'score2': 21},
            {'player1': 'Ира', 'player2': 'Антон Б', 'player3': 'Женя' , 'player4': 'Дима Н','score1': 15, 'score2': 21},
            {'player1': 'Коля', 'player2': 'Гоша', 'player3': 'Макс', 'player4': 'Толик','score1': 21, 'score2': 17},
            {'player1': 'Коля', 'player2': 'Дима Н', 'player3':	'Миша', 'player4': 'Гоша','score1': 21, 'score2': 19},
            {'player1': 'Антон Б', 'player2': 'Толик', 'player3': 'Женя', 'player4': 'Ира','score1': 15, 'score2': 21},
            {'player1': 'Коля', 'player2': 'Женя', 'player3': 'Макс', 'player4': 'Гоша','score1': 12, 'score2': 21},
            {'player1': 'Антон Б', 'player2': 'Дима Н', 'player3': 'Миша', 'player4': 'Толик','score1': 16, 'score2':	21},
            {'player1': 'Ира', 'player2': 'Гоша', 'player3': 'Миша', 'player4': 'Дима Н','score1': 11, 'score2': 21},
            {'player1': 'Коля', 'player2': 'Толик', 'player3': 'Женя', 'player4': 'Макс','score1': 21, 'score2': 14}]

games2 = [{'player1': 'Коля', 'player2': 'Дима Н', 'player3': 'Женя', 'player4': 'Антон Б', 'score1': 21, 'score2': 9},
            {'player1': 'Гоша', 'player2': 'Толик', 'player3': 'Миша', 'player4': 'Макс','score1': 21, 'score2': 17},
            {'player1': 'Макс', 'player2': 'Дима Н', 'player3': 'Коля', 'player4':'Миша','score1': 21, 'score2': 19},
            {'player1': 'Ира', 'player2': 'Гоша', 'player3': 'Женя', 'player4':	'Толик','score1': 15, 'score2': 21},
            {'player1': 'Антон Б', 'player2': 'Гоша', 'player3': 'Коля', 'player4': 'Толик','score1': 8, 'score2': 21},
            {'player1': 'Женя', 'player2': 'Миша', 'player3': 'Макс', 'player4': 'Ира','score1': 21, 'score2':	18},
            {'player1': 'Макс', 'player2': 'Толик', 'player3': 'Ира', 'player4': 'Антон Б','score1': 21, 'score2':	10},
            {'player1': 'Миша', 'player2': 'Дима Н', 'player3': 'Коля', 'player4': 'Женя','score1': 18, 'score2': 21},
            {'player1': 'Миша', 'player2': 'Ира', 'player3': 'Макс', 'player4': 'Антон Б','score1': 12, 'score2': 21},
            {'player1': 'Коля', 'player2': 'Гоша', 'player3': 'Женя', 'player4': 'Дима Н','score1': 19,  'score2':21},
            {'player1': 'Антон Б', 'player2': 'Гоша', 'player3': 'Женя', 'player4': 'Миша','score1': 12, 'score2': 21},
            {'player1': 'Дима Н', 'player2': 'Толик', 'player3': 'Макс', 'player4': 'Ира','score1':	21, 'score2':12},
            {'player1': 'Ира', 'player2': 'Толик', 'player3': 'Коля', 'player4': 'Миша','score1': 14, 'score2': 21},
            {'player1': 'Дима Н', 'player2':	'Гоша', 'player3': 'Макс', 'player4': 'Антон Б','score1': 19, 'score2': 21},
            {'player1': 'Ира', 'player2': 'Антон Б', 'player3': 'Женя' , 'player4': 'Дима Н','score1': 15, 'score2': 21},
            {'player1': 'Коля', 'player2': 'Гоша', 'player3': 'Макс', 'player4': 'Толик','score1': 21, 'score2': 17},
            {'player1': 'Коля', 'player2': 'Дима Н', 'player3':	'Миша', 'player4': 'Гоша','score1': 21, 'score2': 19},
            {'player1': 'Антон Б', 'player2': 'Толик', 'player3': 'Женя', 'player4': 'Ира','score1': 15, 'score2': 21},
            {'player1': 'Коля', 'player2': 'Женя', 'player3': 'Макс', 'player4': 'Гоша','score1': 12, 'score2': 21},
            {'player1': 'Антон Б', 'player2': 'Дима Н', 'player3': 'Миша', 'player4': 'Толик','score1': 16, 'score2':	21},
            {'player1': 'Ира', 'player2': 'Гоша', 'player3': 'Миша', 'player4': 'Дима Н','score1': 11, 'score2': 21},
            {'player1': 'Коля', 'player2': 'Толик', 'player3': 'Женя', 'player4': 'Макс','score1': 21, 'score2': 14}]

Day1 = Day('10.01.2023', games)
Day2 = Day('12.01.2023', games2)
Day1.start_games_counting(Players_Dict)
Day2.start_games_counting(Players_Dict)

#game1.import_players(Players_Dict) #this is for each game
#game1.create_temp_players()  #this is for each game
# #print('Real of pair1 =', game1.real_score_1(), 'Real of pair2 =', game1.real_score_2())
# game1.set_daily_score() #this is after each game
# game1.update_Players_Dict(Players_Dict)
# #print('Current player list in HDD', Players_Dict)
#
# #print('Game2')
# #print('Current player list in HDD', Players_Dict)
# game2.import_players(Players_Dict) #this is for each game
# game2.create_temp_players() #this is for each game
# #print('Real of pair1 =',game2.real_score_1(), 'Real of pair2 =', game2.real_score_2())
# game2.set_daily_score() #this is after each game
# game2.update_Players_Dict(Players_Dict)
# #print('Current player list in HDD', Players_Dict)
#
# game3.import_players(Players_Dict) #this is for each game
# game3.create_temp_players() #this is for each game
# #print('Real of pair1 =', game3.real_score_1(), 'Real of pair2 =', game3.real_score_2())
# game3.set_daily_score() #this is after each game
# game3.update_Players_Dict(Players_Dict)
# #print('Current player list in HDD', Players_Dict)
#
#
# for i in Players_Dict:
#     i['score'] = i['score'] + i['daily_score']
#     i['daily_score'] = 0
#
# print('Day')
# print('After full Day', Players_Dict)


# game1.update_Players_Dict(Players_Dict) #copy all temp in game to total in program
# game1.update_pl_dict(Players_Dict) #copy all temp in game to total in program - Should execute after Day, not after Game
# print(Players_Dict)