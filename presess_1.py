from New_Class import Player, Game

Players_Dict = []

print(Players_Dict)
game1 = Game('Дима Н', 'Толя', 'Гоша', 'Денис', 21, 12)
game1.new()
print(Players_Dict)
print(game1.wait_score_1(), game1.wait_score_2())
print(game1.real_score_1(), game1.real_score_2())
game1.set_daily_score()
print(game1.update_players())
game1.update_pl_dict()
print(Players_Dict)