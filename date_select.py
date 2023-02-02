import time


def validate_date_format(date):
    try:
        time.strptime(date, '%d.%m.%Y')
        return True
    except:
        print(f'Формат даты должен быть "ДД.ММ.ГГГГ", вы ввели "{date}"')
        return False

def date_input():
    while True:
        print()
        game_date = input("Введите дату игр для обновления статистики. Формат ДД.ММ.ГГГГ :")
        if validate_date_format(game_date):
            break
        print('Повторите ввод')
    print(f'Обрабатываем дату {game_date}...')
    return game_date