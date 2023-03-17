import pandas
import json
import time
import os

side1 = 'Левая площадка'


class Import_Excel:

    @staticmethod
    def load(file, sheet):
        # Import_Excel.check_sheet(file, sheet)
        day_data_excel = pandas.read_excel(file, sheet_name=sheet, header=None)
        json_str = day_data_excel.to_json(orient='records', force_ascii=False)
        test = json.loads(json_str)
        return test

    @staticmethod
    def check_none(a):
        if type(a) is not None:
            return a

    @staticmethod
    def check_sheet(file, sheet):
        wb = pandas.read_excel(file, None)
        for i in wb.keys():
            if i == sheet:
                return True
        else:
            print()
            print('ВНИМАНИЕ   В Excel файле (%s) не найдена страница с именем (%s) для этого игрового дня.' % (file, sheet))
            print('           Статистика будет пересчитана без учета этих данных......')
            print()
            #show_sleep_time(2)
            time.sleep(4)
            return False

    @staticmethod
    def check_file_exist(file, sheet):
        if os.path.exists(file):
            return Import_Excel.check_sheet(file, sheet)
        else:
            print()
            print('ВНИМАНИЕ   Excel файл (%s) не найден. Статистика будет пересчитана без учета этих данных.' % (file))
            print()

    @staticmethod
    def check_correct_score(a, b):
        #  Check template score correct  for each game for. In incorrect - False and print description
        if not isinstance(a, int) and isinstance(b, int):
            print()
            print(f'!!!ОШИБКА!!!   Найдена игра с некорректным счетом ({a},{b}), должны быть целые и положительные числа')
            return False
        elif a == b:
            print()
            print(f'!!!ОШИБКА!!!   Найдена игра с некорректным счетом ({a},{b}), счет не может быть равным')
            return False
        elif max(a, b) > 30:
            print()
            print(f'!!!ОШИБКА!!!   Найдена игра с некорректным счетом ({a},{b}), счет не может быть больше 30')
            return False
        elif max(a, b) > 21 and not (max(a, b) - min(a, b)) == 2:
            print()
            print(f'!!!ОШИБКА!!!   Найдена игра с некорректным счетом ({a},{b}), при игре на Больше\Меньше')
            print('               разница в счете должна быть 2 очка')
            return False
        elif max(a, b) == 21 and 19 < min(a, b):
            print()
            print(f'!!!ОШИБКА!!!   Найдена игра с некорректным счетом ({a},{b}), разница в счете должна быть 2 очка')
            return False
        elif max(a, b) < 21:
            print()
            print(f'!!!ОШИБКА!!!   Найдена игра с некорректным счетом ({a},{b}), победитель должен набрать 21 очко')
            return False
        else:
            return True
    @staticmethod
    def open_check_score(test):
        #  Function for parse Excel template and execute def check score.
        for i, j in zip(test, (0, 1)):
            for z, k in zip(i, range(len(i))):
                if i[z] == side1:
                    row = int(j + 1)
                    column = int(k)
                    for m in range(len(test)):
                        if row + 1 < len(test):
                            if Import_Excel.check_none(test[row + 1][str(column + 1)]):
                                a = test[int(row + 1)][str(k + 1)]
                                b = test[int(row + 1)][str(k + 2)]
                                if Import_Excel.check_correct_score(a, b):
                                    row = row + 2
                                else:
                                    return False
        return True


    @staticmethod
    def import_excel(test):
        temp_players = []
        players = []
        for i, j in zip(test, (0, 1)):
            for z, k in zip(i, range(len(i))):
                if i[z] == side1:
                    row = int(j + 1)
                    column = int(k)
                    for m in range(len(test)):
                        if row + 1 < len(test):
                            if Import_Excel.check_none(test[row + 1][str(column + 1)]):
                                a = dict(player1=test[int(row)][str(k)].title(), player2=test[int(row)][str(k + 1)].title(),
                                         player3=test[int(row)][str(k + 2)].title(), player4=test[int(row)][str(k + 3)].title(),
                                         score1=test[int(row + 1)][str(k + 1)], score2=test[int(row + 1)][str(k + 2)])
                                temp_players.append(a)
                                players.extend(temp_players)
                                temp_players = []
                                row = row + 2
        return players


