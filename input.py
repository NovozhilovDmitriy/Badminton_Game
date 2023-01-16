from Badminton_class import Player, Pair, Game, Day

import pandas
import json

day_data_excel = pandas.read_excel('2Расстановки.xlsx', sheet_name='6', header=None)

json_str = day_data_excel.to_json(orient='records', force_ascii=False)
test = json.loads(json_str)

Players = list()
Pl = list()

for key, value in test[0].items():
    if key > '0' and key < '7':
        globals()['player_%s' % key] = Player(value, 500)
        Players.append(globals()['player_%s' % key])
def players_score(player):
    for i in range(len(player)):
        z= (player[i].name, player[i].score)
        Pl.append(z)

players_score(Players)

Pl2 = pandas.DataFrame(Pl)
Pl2.to_excel('Players.xlsx')