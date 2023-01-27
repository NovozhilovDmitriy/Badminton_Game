import DB_SQLite
from New_Class import Player, Game, Day
from input import Import_Excel
import os

stat_file = 'Total_Stat.xlsx'
if os.path.exists((stat_file)):
    print("Excel stat file exist...")
    os.remove(stat_file)
    print("Excel stat file deleted")
else:
    print("Excel stat file not exist, will generated")

Players_Dict = []

date = '21.01.2023'

DB_SQLite.create_table()

if DB_SQLite.check_date(date):  # If no this date in DB table="games" - import. If exist - pass
    games = Import_Excel.load('2Расстановки.xlsx', date)  # Convert excel to dict
    games = Import_Excel.import_excel(games)  # Load dict to Players dict format
    for i in games:
        DB_SQLite.insert_games([date, i['player1'], i['player2'], i['player3'], i['player4'], i['score1'], i['score2']])

#  drop stat table, create stat table
DB_SQLite.drop_table_stat('stat')
DB_SQLite.create_stat_table()
#  Load oldest day games from DB table to dict and process it. Do it for each next day from table.
queue = DB_SQLite.table_date_list()
for i in queue:
    games = DB_SQLite.export_one_day_games(i)
    Day1 = Day(i, games)
    Day1.start_games_counting(Players_Dict)

DB_SQLite.select_stat1()
