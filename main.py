import DB_SQLite
from New_Class import Player, Game, Day
from input import Import_Excel
import date
import os



if __name__ == '__main__':

    # Input date for new game and validate format of this date
    date = date.date_select()

    #date = '31.01.2023'

    #  Temp dict of all players what need to process
    Players_Dict = []

    #  Static name of final report excel file.
    stat_file = 'Total_Stat.xlsx'

    #  Check if report file exist -> delete. If not exist -> will generate new one later
    if os.path.exists((stat_file)):
        print(f'Excel файл статистики ({stat_file}) найден и будет удален...')
        os.remove(stat_file)
        print(f'Excel файл стастики ({stat_file}) удален...')
    else:
        print(f'Excel файл статистики ({stat_file}) не найден и будет создан далее')

    #  Create table games.
    DB_SQLite.create_table_game()

    #  If no this date in DB table="games" - import. If exist - pass
    if DB_SQLite.check_date(date):
        print(f'В статистике нет игр за ({date}) дату. Эти игры будут добавлены из Excel файла (2Расстановки.xlsx) страница ({date})')
        games = Import_Excel.load('2Расстановки.xlsx', date)  #  Convert excel to dict
        games = Import_Excel.import_excel(games)              #  Load dict to Players dict format
        for i in games:                                       #  insert all new games to DB table
            DB_SQLite.insert_games([date, i['player1'], i['player2'], i['player3'], i['player4'], i['score1'], i['score2']])
    print(f'В статистике уже есть игры за ({date}) дату. Игры из из Excel файла (2Расстановки.xlsx) не будут учитываться')

    #  drop stat table, create stat table
    DB_SQLite.drop_table_stat('stat')
    DB_SQLite.create_stat_table()

    #  Load oldest day games from DB table to dict and process it. Do it for each next day from table.
    queue = DB_SQLite.table_date_list()
    for i in queue:
        games = DB_SQLite.export_one_day_games(i)
        Day1 = Day(i, games)
        Day1.start_games_counting(Players_Dict)

    #  Generate all Statistics Excel report
    DB_SQLite.select_stat1()
