from New_Class import Player, Game

Players_Dict = []
#Players_Dict = [{'name': 'Дима Н', 'score': 0}, {'name': 'Гоша', 'score': 10}, {'name': 'Денис', 'score': 100}]

print('Game1')
print('Current player list in HDD', Players_Dict)
game1 = Game('Дима Н', 'Толя', 'Гоша', 'Денис', 21, 12)
game2 = Game('Дима Н', 'Толя', 'Гоша', 'Денис', 12, 21)

game1.import_players(Players_Dict) #this is for each game
game1.create_temp_players() #this is for each game
print('Wait of pair1 =', game1.wait_score_1(), 'Wait of pair2 =', game1.wait_score_2())
print('Real of pair1 =',game1.real_score_1(), 'Real of pair2 =', game1.real_score_2())
game1.set_daily_score() #this is after each game

print('Game2')
print('Current player list in HDD', Players_Dict)
game2.import_players(Players_Dict) #this is for each game
game2.create_temp_players() #this is for each game
print('Wait of pair1 =', game2.wait_score_1(), 'Wait of pair2 =', game2.wait_score_2())
print('Real of pair1 =',game2.real_score_1(), 'Real of pair2 =', game2.real_score_2())
game2.set_daily_score() #this is after each game
print(game2.update_players())


# game1.update_Players_Dict(Players_Dict) #copy all temp in game to total in program
# game1.update_pl_dict(Players_Dict) #copy all temp in game to total in program - Should execute after Day, not after Game
# print(Players_Dict)