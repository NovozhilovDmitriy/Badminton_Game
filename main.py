import time

import DB_SQLite
#from New_Class import Day
import New_Class
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
    if os.path.exists(stat_file):
        print(f'Excel файл статистики ({stat_file}) найден и будет удален...')
        while True:  #  Check if file is open. Loop waiting close file.
            try:
                os.remove(stat_file)
            except OSError:
                print(f'!!!!      Excel  файл  статистики  ({stat_file})  в  данный  момент  ОТКРЫТ')
                print(' !!!!      и не может быть удален программой. Зайкройте файл и повторите операцию')
                input('Нажмите ENTER как будете готовы повторить попытку удаления файла......')
                print('Проверяем........')
                print()
            else:
                print(f'Excel файл статистики ({stat_file}) удален...')
                break

    else:
        print(f'Excel файл статистики ({stat_file}) не найден и будет создан')

    #  Create table games.
    DB_SQLite.create_table_game()

    #  If no this date in DB table="games" - import. If exist - pass
    if DB_SQLite.check_date(date):
        print(f'\n!   В базе нет игр за ({date}) дату.')
        print(f'!   Эти игры будут добавлены из Excel файла ({excel_file}) страница ({date})')
        print()
        time.sleep(4)


       # if Import_Excel.check_sheet(excel_file, date):
        if Import_Excel.check_file_exist(excel_file, date):
            games = Import_Excel.load(excel_file, date)           #  Convert excel to dict
            games = Import_Excel.import_excel(games)              #  Load dict to Players dict format
            for i in games:                                       #  insert all new games to DB table
                DB_SQLite.insert_games([date, i['player1'], i['player2'], i['player3'], i['player4'], i['score1'], i['score2']])
    else:
        print(f'\n!   В базе уже есть игры за ({date}) дату.')
        print(f'!   Игры из из Excel файла ({excel_file}) не будут учитываться')
        print()
        time.sleep(3)

    #  drop stat table, create stat table
    DB_SQLite.drop_table_stat('stat')
    DB_SQLite.create_stat_table()

    #  Load the oldest day games from DB table to dict and process it. Do it for each next day from table.
    queue = DB_SQLite.table_date_list()
    for i in queue:
        games = DB_SQLite.export_one_day_games(i)
        Day1 = New_Class.Day(i, games)
        Day1.start_games_counting(Players_Dict)

    #  Generate all Statistics Excel report
    DB_SQLite.select_stat1()


def date_games_delete():
    #  Delete games from DB with special date
    date = date_select.date_input()

    if DB_SQLite.check_date(date):
        print(f'!!!!   В базе нет игр за ({date}) дату.')
    else:
        count = DB_SQLite.count_games_in_day_from_db(date)
        DB_SQLite.del_games_from_db(date)
        print(f'!!!!   Из базы было удалено ({count[0]}) игр за ({date}) дату')



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

    print('\n\n                  ПРОГРАММА ДЛЯ РАСЧЕТА РЕЙТИНГА ИГРОКОВ И ')
    print('        ВЫЧИСЛЕНИЯ ПОБЕДИТЕЛЯ ПО КОЛИЧЕСТВУ ПОБЕД В ТУРНИРНЫЙ ПЕРИОД')
    print('---------------------------------------------------------------------------------')
    print('Выбрав пункт 1 - Программа  будет расчитывать рейтинг игроков.  Игры заносятся по')
    print('               дням из Excel файла с именем ', read_config('excel_file'))
    print('                 Для корректной  работы программы Excel файл должен быть шаблоном')
    print('               расстановок игр (смотрите шаблон ', read_config('excel_file'), ')')
    print('                 Имя  листа в Excel файле должно быть  ДАТОЙ  игры. Вводимая дата')
    print('               для анализа  должна  совпадать с именем  листа в Excel файле. Даты')
    print('               можно  добавлять  в  любой   последовательности,  если  необходимо')
    print('               обработать несколько дней. Окончательный результат игр будет после')
    print('               добавления всех дат')
    print('Выбрав пункт 2 - Вы  можете  удалить из базы игры за любой  день указав дату. Это')
    print('               может быть  неоходимо,  если  при  добавлении  игр  шаблоном  было')
    print('               добавлено   неправильное   имя   игрока  или  счет,  или  возникла')
    print('               какая-либо ошибка в ходе выполнения пункта 1')
    print('Выбрав пункт 0 - Выход  из  программы.  Все  операции,  которые были выполнены до')
    print('               этого, будут сохранены')
    print('\n               version 09.02.2023')
    print('---------------------------------------------------------------------------------')
    print()


    while True:
        print('\n    Главное Меню ')
        print('1.  Ввод данных и расчет рейтинга')
        print('2.  Редактирование базы игр (удаление игрового дня)')
        print('0.  Выход из программы')
        print()
        cmd = input('Выберите пункт: ')
        print()

        if cmd == '0':
            break
        elif cmd == '1':
            data_analyse()
        elif cmd == '2':
            date_games_delete()
        else:
            print('\n Попробуйте еще раз')
            print()

