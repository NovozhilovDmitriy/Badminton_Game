import time

import DB_SQLite
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

    #  Value for MAX_MIN def. Player score.
    max_score = 0           #  This is start of max score. For chart report
    min_score = 10000       #  This is start of min score. For chart report

    #  Check if report file exist -> delete. If not exist -> will generate new one later
    if os.path.exists(stat_file):
        print(f'Excel файл статистики ({stat_file}) найден и будет удален...')
        while True:  #  Check if file is open. Loop waiting close file.
            try:
                os.remove(stat_file)
            except OSError:
                print(f'!!!ОШИБКА!!!      Excel  файл  статистики  ({stat_file})  в  данный  момент  ОТКРЫТ')
                print(f'                  и не может быть удален программой. Зайкройте файл и повторите операцию')
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
        print()
        print(f'ВНИМАНИЕ   В базе нет игр за ({date}) дату.')
        print(f'           Эти игры будут добавлены из Excel файла ({excel_file})')
        print(f'           Проверям наличие страницы ({date}) и корректность заполнения счета игр.......')
        #time.sleep(2)
        show_sleep_time(2)
        if Import_Excel.check_file_exist(excel_file, date):
                games = Import_Excel.load(excel_file, date)               #  Convert excel to dict
                if Import_Excel.open_check_score(games):                  #  Check template game score. If incorrect - ignore import
                    #games = Import_Excel.load(excel_file, date)          #  Convert excel to dict
                    games = Import_Excel.import_excel(games)              #  Load dict to Players dict format
                    for i in games:                                       #  insert all new games to DB table
                        DB_SQLite.insert_games([date, i['player1'], i['player2'], i['player3'], i['player4'], i['score1'], i['score2']])

                else:
                    print('ВНИМАНИЕ   В статистике есть игры с некорректным счетом, ВСЕ игры этого дня НЕ учитываются при расчете')
                    print('           Продолжаем расчет статистики.......')
                    print()
                    show_sleep_time(4)
                    #time.sleep(4)
    else:
        print(f'\nВНИМАНИЕ   В базе уже есть игры за ({date}) дату.')
        print(f'           Игры из из Excel файла ({excel_file}) не будут учитываться')
        print(f'           Продолжаем расчет статистики.......')
        print()
        show_sleep_time(3)
        #time.sleep(3)

    #  drop stat table, create stat table
    DB_SQLite.drop_table_stat('stat')
    DB_SQLite.create_stat_table()

    #  Load the oldest day games from DB table to dict and process it. Do it for each next day from table.
    queue = DB_SQLite.table_date_list()

    for i in queue:
        games = DB_SQLite.export_one_day_games(i)
        Day1 = New_Class.Day(i, games)
        Day1.start_games_counting(Players_Dict)
        max_score = max(max_score, max_min_score(Players_Dict)[0])  #  Find max player score for chart report
        min_score = min(min_score, max_min_score(Players_Dict)[1])  #  Find min player score for chart report
    #  Generate all Statistics Excel report
    #  max_min_score(Players_Dict)
    #  DB_SQLite.select_stat1(max_min_score(Players_Dict)[0], max_min_score(Players_Dict)[1])
    DB_SQLite.select_stat1(max_score, min_score)


def max_min_score(Players_Dict):
    #  Find MAX players score and MIN player score in DB and return result. Need for print correct Chart in report.
    max_score = max(enumerate(Players_Dict), key=lambda arg:arg[1]['score'])[0]
    min_score = min(enumerate(Players_Dict), key=lambda arg:arg[1]['score'])[0]
    return int(Players_Dict[max_score]['score']) + 5, int(Players_Dict[min_score]['score']) - 5


def show_sleep_time(t):
    for i in range(t, 0, -1):
        #print(f"Продолжим через {i}")
        print(f"{i}..", end = "")
        time.sleep(1)


def date_games_delete():
    #  Delete games from DB with special date
    date = date_select.date_input()

    if DB_SQLite.check_date(date):
        print(f'ВНИМАНИЕ   В базе нет игр за ({date}) дату.')
    else:
        count = DB_SQLite.count_games_in_day_from_db(date)
        DB_SQLite.del_games_from_db(date)
        print(f'ВНИМАНИЕ   Из базы было удалено ({count[0]}) игр за ({date}) дату')



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
    elif conf_data == 'ch_active':
        return int(config['Championship']['active_players'])
    elif conf_data == 'ch_percent':
        return float(config['Championship']['percent'])
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
    print('\n               version 31.03.2023')
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

