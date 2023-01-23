from New_Class import Player, Game

Players_Dict = []
#Players_Dict = [{'name': 'Дима Н', 'score': 500,'daily_score': 0}]

print('Game1')
print('Current player list in HDD', Players_Dict)
game1 = Game('Дима Н', 'Толя', 'Гоша', 'Денис', 21, 12)
game2 = Game('Миша', 'Толя', 'Гоша', 'Денис', 21, 12)
game3 = Game('Коля', 'Толя', 'Гоша', 'Денис', 21, 12)

game1.import_players(Players_Dict) #this is for each game
game1.create_temp_players() #this is for each game
print('Real of pair1 =', game1.real_score_1(), 'Real of pair2 =', game1.real_score_2())
game1.set_daily_score() #this is after each game
game1.update_Players_Dict(Players_Dict)
print('Current player list in HDD', Players_Dict)

print('Game2')
print('Current player list in HDD', Players_Dict)
game2.import_players(Players_Dict) #this is for each game
game2.create_temp_players() #this is for each game
print('Real of pair1 =',game2.real_score_1(), 'Real of pair2 =', game2.real_score_2())
game2.set_daily_score() #this is after each game
game2.update_Players_Dict(Players_Dict)
print('Current player list in HDD', Players_Dict)

game3.import_players(Players_Dict) #this is for each game
game3.create_temp_players() #this is for each game
print('Real of pair1 =', game3.real_score_1(), 'Real of pair2 =', game3.real_score_2())
game3.set_daily_score() #this is after each game
game3.update_Players_Dict(Players_Dict)
print('Current player list in HDD', Players_Dict)


for i in Players_Dict:
    i['score'] = i['score'] + i['daily_score']
    i['daily_score'] = 0

print('Day')
print('After full Day', Players_Dict)


# game1.update_Players_Dict(Players_Dict) #copy all temp in game to total in program
# game1.update_pl_dict(Players_Dict) #copy all temp in game to total in program - Should execute after Day, not after Game
# print(Players_Dict)