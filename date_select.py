import time
import datetime


def validate_date_format(date):
    try:
        time.strptime(date, '%Y-%m-%d')
        return True
    except:
        print(f'Формат даты должен быть "ГГГГ-ММ-ДД", вы ввели "{date}"')
        return False

def validate_short_date(date):
    temp = date.split('-')
    if len(temp[1]) == 2 and len(temp[2]) == 2:
        return True
    else:
        print(f'Формат даты должен быть "ГГГГ-ММ-ДД", вы ввели "{date}"')
        return False

# def convert_date(date):
#     temp = datetime.datetime.strptime(date, "%d.%m.%Y").strftime("%Y-%m-%d")
#     print(temp)
#     return temp

def date_input():
    while True:
        print()
        game_date = input("Введите дату игр для обновления статистики. Формат ГГГГ-ММ-ДД :")
        if validate_date_format(game_date) and validate_short_date(game_date):
            break
        print('Повторите ввод')
    #game_date = convert_date(game_date)
    print(f'Обрабатываем дату {game_date}...')
    return game_date
