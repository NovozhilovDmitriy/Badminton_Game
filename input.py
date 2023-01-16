from Badminton_class import Player, Pair, Game, Day

import pandas
import json

day_data_excel = pandas.read_excel('2Расстановки.xlsx', sheet_name='5', header=None)

json_str = day_data_excel.to_json(orient='records', force_ascii=False)
test = json.loads(json_str)

# tt = test[0].value(1)
#ttt = tt[1]
# for i in test:
#     for key, value in i.items():
#         if key != '0':
#             globals()['player_%s' % key] = Player(value, 500)

# temp_i = list(range(1, 6))
for key, value in test[0].items():
    if key > '0' and key < '6':
        globals()['player_%s' % key] = Player(value, 500)

# for i in temp_i:
#     globals()['player_%s' % i] = Player(tt[i], 500)

# def players_score(player):
#     for i in range(len(player)):
#         print('Score ', player[i].name, ' = ', player[i].score, 'Daily score = ', player[i].daily_score)
#
# players_score(Players)