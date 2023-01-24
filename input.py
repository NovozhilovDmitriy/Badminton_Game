import pandas
import json

day_data_excel = pandas.read_excel('2Расстановки.xlsx', sheet_name='8', header=None)

json_str = day_data_excel.to_json(orient='records', force_ascii=False)
test = json.loads(json_str)

Players = []
temp_players = []
Pl = list()

side1 = 'Левая площадка'

def check_none(a):
    if type(a) is not None:
        return a


for i, j in zip(test, (0,1)):
    for z, k in zip(i, range(len(i))):
        if i[z] == side1:
            row = int(j+1)
            column = int(k)
            if row <= len(test):
                for m in range(len(test)):
                    if check_none(test[row+1][str(column+1)]):
                        temp_players.append(dict(player1=test[int(row)][str(k)],player2=test[int(row)][str(k+1)],player3=test[int(row)][str(k+2)],player4=test[int(row)][str(k+3)], score1=test[int(row+1)][str(k+1)], score2=test[int(row+1)][str(k+2)]))
                        Players.extend(temp_players)
                        temp_players = []
                        row = row + 2

                row = row + 2


print(Players)


#players_score(Players)

# Pl2 = pandas.DataFrame(Pl)
# Pl2.to_excel('Players.xlsx')

#a = 2
# for key, value in test[a].items():
#     if key > '0' and key < '7':
#         globals()['player_%s' % key] = Player(value, 500)
#         Players.append(globals()['player_%s' % key])