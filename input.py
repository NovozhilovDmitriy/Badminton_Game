from Badminton_class import Player

import pandas
import json

day_data_excel = pandas.read_excel('2Расстановки.xlsx', sheet_name='6', header=None)

json_str = day_data_excel.to_json(orient='records', force_ascii=False)
test = json.loads(json_str)

Players = []
temp_players = []
Pl = list()

side1 = 'Левая площадка'
side2 = 'Правая площадка'
def check_none(a):
    if type(a) != int:
        return None
    else:
        return None

for i, j in zip(test, (0,1,2)) :
    for z, k in zip(i, range(len(i))):
        if i[z] == side1:
            row = int(j+1)
            column = int(k)
            for m in range(len(test)):
                check_none(test[m][str(column+1)])
                temp_players.append(dict(player1=test[int(row)][str(k)],player2=test[int(row)][str(k+1)],player3=test[int(row)][str(k+2)],player4=test[int(row)][str(k+3)], score1=test[int(row+1)][str(k+1)], score2=test[int(row+1)][str(k+2)]))
                Players.extend(temp_players)
                temp_players = []
                row = row + 2


print(Players)


#
# check = check_none(test[int(3)][str(2)])

#Создал игроков из экселя строки 0
# for key, value in test[0].items():
#     if '7' > key > '0':
#         globals()['player_%s' % key] = Player(value, 500)
#         Players.append(globals()['player_%s' % key])
# def players_score(player):
#     for i in range(len(player)):
#         z = (player[i].name, player[i].score)
#         Pl.append(z)

#players_score(Players)

# Pl2 = pandas.DataFrame(Pl)
# Pl2.to_excel('Players.xlsx')

#a = 2
# for key, value in test[a].items():
#     if key > '0' and key < '7':
#         globals()['player_%s' % key] = Player(value, 500)
#         Players.append(globals()['player_%s' % key])