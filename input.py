from Badminton_class import Player, Pair, Game, Day

import pandas
import json

day_data_excel = pandas.read_excel('2Расстановки.xlsx', sheet_name='5', header=None)

json_str = day_data_excel.to_json(orient='records')
test = json.loads(json_str)
print()
