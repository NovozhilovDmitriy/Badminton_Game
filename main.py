import DB_SQLite
from New_Class import Day
from input import Import_Excel
import date_select
import os
import configparser



def data_analyse():

    # Get Excel file name from INI file

    excel_file = read_config('excel_file')

    # Input date for new game and validate format of this date
    date = date_select.date_input()

    #date = '31.01.2023'

    #  Temp dict of all players what need to process
    Players_Dict = []

    #  Static name of final report excel file.
    stat_file = 'Total_Stat.xlsx'

    #  Check if report file exist -> delete. If not exist -> will generate new one later
    if os.path.exists((stat_file)):
        print(f'Excel файл статистики ({stat_file}) найден и будет удален...')
        os.remove(stat_file)
        #print(f'Excel файл стастики ({stat_file}) удален...')
    else:
        print(f'Excel файл статистики ({stat_file}) не найден и будет создан')

    #  Create table games.
    DB_SQLite.create_table_game()

    #  If no this date in DB table="games" - import. If exist - pass
    if DB_SQLite.check_date(date):
        print(f'!   В базе нет игр за ({date}) дату. Эти игры будут добавлены из Excel файла ({excel_file}) страница ({date})')
        print()
        if Import_Excel.check_sheet(excel_file, date):
            games = Import_Excel.load(excel_file, date)  #  Convert excel to dict
            games = Import_Excel.import_excel(games)              #  Load dict to Players dict format
            for i in games:                                       #  insert all new games to DB table
                DB_SQLite.insert_games([date, i['player1'], i['player2'], i['player3'], i['player4'], i['score1'], i['score2']])
    else:
        print(f'!   В базе уже есть игры за ({date}) дату. Игры из из Excel файла ({excel_file}) не будут учитываться')
        print()

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

    #input()

def date_games_delete():
    #  Delete games from DB with special date
    date = date_select.date_input()

    if DB_SQLite.check_date(date):
        print(f'!!!!   В базе нет игр за ({date}) дату.')
    else:
        DB_SQLite.del_games_from_db(date)
        print(f'!!!!   Все игры за ({date}) дату удалены из базы')



def read_config(conf_data):
    #  Read config file for choose parameters
    config = configparser.ConfigParser()
    config.read('conf.ini')
    if conf_data == 'excel_file':
        return config['EXCEL']['workbook']
    elif conf_data == 'ch_start':
        return config['Championship']['start_day']
    elif conf_data == 'ch_end':
        return config['Championship']['end_day']
    else:
        return False

if __name__ == '__main__':

    print()
    print()
    print('Программа для расчета рейтинга игроков и вычисления победителя по количеству побед в турнирный период')
    print('---------------------------------------------------------------------------------------------------------')
    print('Выбрав пункт 1 - Программа будет расчитывать рейтинг игроков. Игры заносятся по дням из Excel файл с именем ', read_config('excel_file'))
    print('         Для корректной работы программы Excel файл должен быть шаблоном растановок игр (смотрите шаблон ', read_config('excel_file'))
    print('         Имя листа в Excel файле должно быть ДАТОЙ игры. Вводимая дата для анализа должна совпадать с именем листа в Excel файле')
    print('         Даты можно вводить в любом порядке, если необходимо обработать несколько дней. Но корректный результат будет после добавления всех дат')
    print('Выбрав пункт 2 - Вы можете удалить из базы игр любой день указав дату. Это может быть неоходимо если при добавлении ирг шаблоном было')
    print('         добавлено неправильное имя игрока либо счет или возникла какая либо ошибка в ходе выполнения пункта 1')
    print('Выбрав пункт 0 - Вы закроете программу. Все операции, которые были выполнены до этого, будут сохранены')
    print()
    print('version 03.02.2023')
    print('--------------------------------------------------------------------------------------------------------')
    print()


    while True:
        print()
        print('    Главное Меню ')
        print('1.  Ввод данных и расчет рейтинга')
        print('2.  Редактирование базы игр (удаление игрового дня)')
        print('0.  Выход из программы')
        print()
        cmd=input('Выберите пункт: ')
        print()

        if cmd == '0':
            break
        elif cmd == '1':
            data_analyse()
        elif cmd == '2':
            date_games_delete()
        else:
            print()
            print('Попробуйте еще раз')
            print()

