import sqlite3
from sqlite3 import Error
from xlsxwriter.workbook import Workbook

import pandas


def create_table():
    sqlite_connection = sqlite3.connect('list_of_games.db')
    games_table = '''CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY,
                    date DATE FORMAT 'dd.mm.yyyy' NOT NULL,
                    player1 TEXT NOT NULL,
                    player2 TEXT NOT NULL,
                    player3 TEXT NOT NULL,
                    player4 TEXT NOT NULL,
                    score1 INTEGER NOT NULL,
                    score2 INTEGER NOT NULL);'''
    players_score = '''CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    score REAL NOT NULL,
                    daily_score REAL NOT NULL);'''
    cursor = sqlite_connection.cursor()
    cursor.execute(games_table)
    cursor.execute(players_score)
    sqlite_connection.commit()
    cursor.fetchall()
    print('Table games and table score created (if not exist)')
    cursor.close()

def create_stat_table():
    sqlite_connection = sqlite3.connect('list_of_games.db')
    stat_table = '''CREATE TABLE IF NOT EXISTS stat (
                        id INTEGER PRIMARY KEY,
                        date DATE FORMAT 'dd.mm.yyyy' NOT NULL,
                        player1 TEXT NOT NULL,
                        pl1_sum_daily_score REAL NOT NULL,
                        pl1_current_score REAL NOT NULL,
                        player2 TEXT NOT NULL,
                        pl2_sum_daily_score REAL NOT NULL,
                        pl2_current_score REAL NOT NULL,
                        socre1 INTEGER NOT NULL,
                        pair1_avr_score REAL NOT NULL,
                        pair1_Ea REAL NOT NULL,
                        pair1_Sa REAL NOT NULL,
                        pair1_Ra REAL NOT NULL,
                        player3 TEXT NOT NULL,
                        pl3_sum_daily_score REAL NOT NULL,
                        pl3_current_score REAL NOT NULL,
                        player4 TEXT NOT NULL,
                        pl4_sum_daily_score REAL NOT NULL,
                        pl4_current_score REAL NOT NULL,
                        socre2 INTEGER NOT NULL,
                        pair2_avr_score REAL NOT NULL,
                        pair2_Ea REAL NOT NULL,
                        pair2_Sa REAL NOT NULL,
                        pair2_Ra REAL NOT NULL);'''
    cursor = sqlite_connection.cursor()
    cursor.execute(stat_table)
    sqlite_connection.commit()
    cursor.fetchall()
    print('Table stat created (if not exist)')
    cursor.close()


#create_table()
def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :return: Connection object or None
    """
    db_file = 'list_of_games.db'
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def drop_table_stat(table):

    conn = create_connection()
    sql = f"""DROP table IF EXISTS {table}"""

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def insert_games(task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    conn = create_connection()
    sql = ''' INSERT INTO games(date,player1,player2,player3,player4,score1,score2)
              VALUES(?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def insert_stat(task):

    # create a database connection
    conn = create_connection()

    sql = ''' INSERT INTO stat(date,player1,pl1_sum_daily_score,pl1_current_score,
                                    player2,pl2_sum_daily_score,pl2_current_score,
                            socre1,pair1_avr_score,pair1_Ea,pair1_Sa,pair1_Ra,
                                    player3,pl3_sum_daily_score,pl3_current_score,
                                    player4,pl4_sum_daily_score,pl4_current_score,
                            socre2,pair2_avr_score,pair2_Ea,pair2_Sa,pair2_Ra)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def insert_player(task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    conn = create_connection()
    sql = ''' INSERT INTO players(name,score,daily_score)
              VALUES(?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def check_date(date):
    # create a database connection
    conn = create_connection()
    sql = ''' select date from games where date = (?) '''
    cur = conn.cursor()
    cur.execute(sql, (date,))
    result = cur.fetchall()
    if len(result) == 0:
        return True
    else:
        return False

def table_date_list():
    # create a database connection
    conn = create_connection()
    sql = ''' select distinct date from games order by date asc; '''
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return list(result)

def export_one_day_games(date):
    # create a database connection
    conn = create_connection()
    sql = ''' select player1,player2,player3,player4,score1,score2 from games where date = ? order by id asc ;'''
    conn.row_factory = sqlite3.Row
    values = conn.execute(sql, (date,)).fetchall()
    list = []
    for item in values:
        list.append({k: item[k] for k in item.keys()})
    return list

def select_stat1():

    Players_Last_Day_Stat = '''with t1 as
( select id, date, player1 player, player2 partner, pair1_avr_score pair_avr_score, pair1_Ea Ea, pair1_Sa Sa, pair1_Ra Ra, sign(pair1_Ra) win, sign(case when pair1_Ra > -1 and pair1_Ra < 1 then pair1_Ra end) tie_win from stat t
union all select id, date, player2 player, player1 partner, pair1_avr_score, pair1_Ea, pair1_Sa, pair1_Ra, sign(pair1_Ra) win, sign(case when pair1_Ra > -1 and pair1_Ra < 1 then pair1_Ra end) tie_win from stat t
union all select id, date, player3 player, player4 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra, sign(pair2_Ra) win, sign(case when pair1_Ra > -1 and pair1_Ra < 1 then pair1_Ra end) tie_win from stat t
union all select id, date, player4 player, player3 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra, sign(pair2_Ra) win, sign(case when pair1_Ra > -1 and pair1_Ra < 1 then pair1_Ra end) tie_win from stat t
)
select player
     , sum(Ra) last_date_Ra --дельта счета за этот день
     , count(case when win = 1 then 1 end) cnt_win -- количество побед
     , count(case when win = -1 then 1 end) cnt_lost -- количество поражений
     , count(case when tie_win = 1 then 1 end) cnt_tie_win -- количество больше-меньше побед
     , count(case when tie_win = -1 then 1 end) cnt_tie_lost -- количество больше-меньше поражений
     , count(*) cnt_game -- количество всего игр 
  from t1
  where date = (select max(date) from stat)
  group by player
  order by sum(Ra) desc;'''

    Players_Total_Stat = ''' with d as
( select distinct date from stat
), pl as
( select player, min(date) min_date from (select date, player1 player from stat union all select date, player2 from stat union all select date, player3 from stat union all select date, player4 from stat) group by player
), t1 as
( select id, date, player1 player, player2 partner, pair1_avr_score pair_avr_score, pair1_Ea Ea, pair1_Sa Sa, pair1_Ra Ra from stat t
union all select id, date, player2 player, player1 partner, pair1_avr_score, pair1_Ea, pair1_Sa, pair1_Ra from stat t
union all select id, date, player3 player, player4 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
union all select id, date, player4 player, player3 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
), t2 as
( select pl.player
       , d.date
       , sum(t1.Ra) last_date_Ra
       , sum(count(t1.Ra)) over (partition by pl.player order by d.date) cnt_game
       , max(case when sum(t1.Ra) is not null then d.date end) over (partition by pl.player) player_last_date
       , 500 + sum(sum(t1.Ra)) over (partition by pl.player order by d.date) score
       , max(d.date) over () last_date
    from d cross join pl
         left outer join t1 on t1.date = d.date and t1.player = pl.player and d.date >= pl.min_date  
    group by pl.player, d.date
), t3 as
( select t2.*
       , rank() over (partition by date order by score desc) player_rank
    from t2
), t4 as
( select t3.*
       , lag(player_rank) over (partition by player order by date) lag_player_rank
    from t3
)
select player                                                     -- игрок
     , score                                                      -- текущий рейтинг
     , last_date_Ra                                               -- дельту прироста за последнюю дату
     , cnt_game                                                   -- сколько игр было сыграно
     , player_last_date                                           -- датой когда этот игрок играл последний раз
     , case when lag_player_rank <> player_rank then lag_player_rank-player_rank end diff_rank -- динамика
  from t4
  where date = last_date
  order by score desc;'''

    Players_win_pair_stat = '''with t1 as
    ( select id, date, player1 player, player2 partner, pair1_avr_score pair_avr_score, pair1_Ea Ea, pair1_Sa Sa, pair1_Ra Ra, sign(pair1_Ra) win from stat t
    union all select id, date, player2 player, player1 partner, pair1_avr_score, pair1_Ea, pair1_Sa, pair1_Ra, sign(pair1_Ra) win from stat t
    union all select id, date, player3 player, player4 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra, sign(pair2_Ra) win from stat t
    union all select id, date, player4 player, player3 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra, sign(pair2_Ra) win from stat t
    )
    select player, partner
         , count(*)
         , coalesce(sum(case when win>0 then 1 end), 0) cnt_win
         , coalesce(sum(case when win<0 then 1 end), 0) cnt_lost
         , 100*coalesce(sum(case when win>0 then 1 end), 0)/count(*) pct_win
      from t1
      group by player, partner
      having count(*) > 2
      order by player, pct_win desc;'''

    Players_win_opponent_stat = '''with t1 as
    ( select id, date, player1 player, player3 opponent, sign(pair1_Ra) win from stat t
    union all select id, date, player1 player, player4 opponent, sign(pair1_Ra) win from stat t
    union all select id, date, player2 player, player3 opponent, sign(pair1_Ra) win from stat t
    union all select id, date, player2 player, player4 opponent, sign(pair1_Ra) win from stat t
    union all select id, date, player3 player, player1 opponent, sign(pair2_Ra) win from stat t
    union all select id, date, player3 player, player2 opponent, sign(pair2_Ra) win from stat t
    union all select id, date, player4 player, player1 opponent, sign(pair2_Ra) win from stat t
    union all select id, date, player4 player, player2 opponent, sign(pair2_Ra) win from stat t
    )
    select player, opponent
         , count(*)
         , coalesce(sum(case when win>0 then 1 end), 0) cnt_win
         , coalesce(sum(case when win<0 then 1 end), 0) cnt_lost
         , 100*coalesce(sum(case when win>0 then 1 end), 0)/count(*) pct_win
      from t1
      group by player, opponent
      having count(*) > 2
      order by player, pct_win desc;'''

    # Players_daily2_stat = '''with t1 as
    # ( select id, date, player1 player, player2 partner, pair1_avr_score pair_avr_score, pair1_Ea Ea, pair1_Sa Sa, pair1_Ra Ra from stat t
    # union all select id, date, player2 player, player1 partner, pair1_avr_score, pair1_Ea, pair1_Sa, pair1_Ra from stat t
    # union all select id, date, player3 player, player4 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
    # union all select id, date, player4 player, player3 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
    # )
    # select player
    #      , date
    #      , 500 + sum(sum(Ra)) over (partition by player order by date) score -- текущий рейтинг
    #      , sum(count(*)) over (partition by player order by date) cnt_game -- сколько игр было сыграно
    #   from t1
    #   group by player, date
    #   order by player, date;'''

    Players_daily_stat = '''with d as
    ( select distinct date from stat
    ), pl as
    ( select distinct player from (select player1 player from stat union all select player2 from stat union all select player3 from stat union all select player4 from stat)
    ), t1 as
    ( select id, date, player1 player, player2 partner, pair1_avr_score pair_avr_score, pair1_Ea Ea, pair1_Sa Sa, pair1_Ra Ra from stat t
    union all select id, date, player2 player, player1 partner, pair1_avr_score, pair1_Ea, pair1_Sa, pair1_Ra from stat t
    union all select id, date, player3 player, player4 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
    union all select id, date, player4 player, player3 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
    ) 
    select d.date
         , pl.player
         , case when count(Ra) <> 0 then 500 + coalesce(sum(sum(Ra)) over (partition by pl.player order by d.date), 0) end score -- текущий рейтинг
      from d cross join pl
           left outer join t1 on t1.date = d.date and t1.player = pl.player
      group by pl.player, d.date
      order by pl.player, d.date;'''

    from xlsxwriter.workbook import Workbook
    workbook = Workbook('Total_Stat.xlsx')
    conn = create_connection()
    c=conn.cursor()
    def_fmt = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'border': 2

    })

    def_fmt_color = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'border': 2,
        'num_format': '[Green]General;[Red]-General;General'

    })
    #def_fmt_color.set_num_format('[Green]General;[Red]-General;General')

    bold_fmt = workbook.add_format({
        'bold': True,
        'align': 'center',
        'valign': 'vcenter',
        'border': 2
    })
    bold_fmt.set_font_size(13)

    head_fmt = workbook.add_format({
        'bold': True,
        'align': 'center',
        'valign': 'vcenter',
        'border': 2,
    })
    head_fmt.set_bg_color('gray')
    head_fmt.set_font_size(14)

    #  Description worksheet creation
    worksheet = workbook.add_worksheet('Описание')
    worksheet.insert_image('A1', '1_desc.jpg')
    worksheet.insert_image('A16', '2_desc.jpg')
    worksheet.insert_image('A32', '3_desc.jpg')


    #  Last-Day worksheet creation
    worksheet = workbook.add_worksheet('Last-Day')
    mysel = c.execute(Players_Last_Day_Stat)
    header = ['Место', 'Игрок', 'Дельта', 'Победы', 'Поражения', 'Win-ma/mi', 'Loss-ma/mi', 'Всего Игр']
    for idx, col in enumerate(header):
        worksheet.write(0, idx, col, head_fmt)  # write the column name one time in a row

    # write all data from SELECT. keep 1 row and 1 column NULL
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            if isinstance(value, float):
                value = int(value)
            worksheet.write(i + 1, j + 1, value, def_fmt)

    worksheet.write_column(1, 0, [i for i in range(1, len(c.execute(Players_Last_Day_Stat).fetchall()) + 1)], head_fmt)  # make and insert column 1 with index

    worksheet.set_column('B:B', 18)
    worksheet.set_column('C:H', 11)
    #worksheet.autofit()

    worksheet = workbook.add_worksheet('Total')
    mysel=c.execute(Players_Total_Stat)
    header = ['Место', 'Игрок', 'Рейтинг', 'Дельта', 'Всего Игр', 'Последняя Игра', 'Динамика']
    for idx, col in enumerate(header):
        worksheet.write(0, idx, col, head_fmt)  # write the column name one time in a row

    # write all data from SELECT. keep 1 row and 1 column NULL
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            if j == 5:
                worksheet.write(i + 1, j + 1, value, def_fmt_color)
            elif j == 0:
                worksheet.write(i + 1, j + 1, value, bold_fmt)

            elif isinstance(value, float):
                value = int(value)
                worksheet.write(i + 1, j + 1, value, def_fmt)
            else:
                worksheet.write(i + 1, j + 1, value, def_fmt)

    worksheet.write_column(1, 0, [i for i in range(1, len(c.execute(Players_Total_Stat).fetchall()) + 1)], head_fmt)  # make and insert column 1 with index

    worksheet.set_column('B:B', 18)
    worksheet.set_column('C:G', 11)
    worksheet.set_column('F:F', 18)


    worksheet = workbook.add_worksheet('Pair-Win')
    mysel=c.execute(Players_win_pair_stat)
    header = ['Игрок', 'Партнер', 'Всего Игр', 'Побед', 'Поражений', '% Побед']
    for idx, col in enumerate(header):
        worksheet.write(0, idx, col, head_fmt)  # write the column name one time in a row

    # write all data from SELECT. keep 1 row and 1 column NULL
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            if isinstance(value, float):
                value = int(value)
            worksheet.write(i + 1, j, value, def_fmt)

    # worksheet.write_column(1, 0, [i for i in range(1, len(c.execute(Players_win_pair_stat).fetchall()) + 1)])  # make and insert column 1 with index

    # here, we make both 1st column/row bold
    worksheet.set_column('A:B', 18)
    worksheet.set_column('C:F', 11)
    worksheet.autofilter(0, 0, 0, 0)


    worksheet = workbook.add_worksheet('Opponent-Win')
    mysel=c.execute(Players_win_opponent_stat)
    header = ['Игрок', 'Соперник', 'Всего Игр', 'Побед', 'Поражений', '% Побед']
    for idx, col in enumerate(header):
        worksheet.write(0, idx, col, head_fmt)  # write the column name one time in a row

    # write all data from SELECT. keep 1 row and 1 column NULL
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            if isinstance(value, float):
                value = int(value)
            worksheet.write(i + 1, j, value, def_fmt)

    #worksheet.write_column(1, 0, [i for i in range(1, len(c.execute(Players_win_opponent_stat).fetchall()) + 1)])  # make and insert column 1 with index

    # here, we make both 1st column/row bold
    worksheet.set_column('A:B', 18)
    worksheet.set_column('C:F', 11)
    worksheet.autofilter(0, 0, 0, 0)


    worksheet = workbook.add_worksheet('Daily')
    mysel = c.execute(Players_daily_stat)

    r = 1
    cl = 0
    name = ''
    dt = ''
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            if j == 0:
                if i == 0:
                    dt = value
                    worksheet.write(r, 0, value)
                if value != dt:
                    worksheet.write(r, 0, value)
            elif j == 1:
                if value != name:
                    cl += 1
                    r = 1
                    name = value
                    worksheet.write(0, cl, value)
            elif j == 2:
                if isinstance(value, float):
                    value = int(value)
                    worksheet.write(r, cl, value)
        r += 1

    chart = workbook.add_chart({'type': 'line'})
    # Configure the series of the chart from the dataframe data.
    for i in range(cl):
        col = i + 1
        chart.add_series({
            'name': ['Daily', 0, col-1],
            'categories': ['Daily', 1, 0, r, 0],
            'values': ['Daily', 1, col-1, r, col-1],
        })

    # Configure the chart axes.
    chart.set_x_axis({'name': 'дата игры'})
    chart.set_y_axis({'name': 'Рейтинг'})
                      #'major_gridlines': {'visible': False}})
    chart.set_legend({'position': 'top'})
    chart.show_blanks_as('span')
    chart.set_size({'width': 1200, 'height': 580})
    # Insert the chart into the worksheet.
    worksheet.insert_chart('C3', chart)

    workbook.close()


def select_stat2():
    Players_daily_stat = '''with d as
    ( select distinct date from stat
    ), pl as
    ( select distinct player from (select player1 player from stat union all select player2 from stat union all select player3 from stat union all select player4 from stat)
    ), t1 as
    ( select id, date, player1 player, player2 partner, pair1_avr_score pair_avr_score, pair1_Ea Ea, pair1_Sa Sa, pair1_Ra Ra from stat t
    union all select id, date, player2 player, player1 partner, pair1_avr_score, pair1_Ea, pair1_Sa, pair1_Ra from stat t
    union all select id, date, player3 player, player4 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
    union all select id, date, player4 player, player3 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
    ) 
    select d.date
         , pl.player
         , case when count(Ra) <> 0 then 500 + coalesce(sum(sum(Ra)) over (partition by pl.player order by d.date), 0) end score -- текущий рейтинг
      from d cross join pl
           left outer join t1 on t1.date = d.date and t1.player = pl.player
      group by pl.player, d.date
      order by pl.player, d.date;'''

    from xlsxwriter.workbook import Workbook

    workbook = Workbook('Total_Stat.xlsx')
    worksheet = workbook.add_worksheet('Daily')

    conn = create_connection()
    c = conn.cursor()
    mysel = c.execute(Players_daily_stat)

    r = 1
    cl = 0
    name = ''
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            # if isinstance(value, float):
            #     value = int(value)
            if j == 0:
                worksheet.write(r, 0, value)
            elif j == 1:
                if value != name:
                    cl += 1
                    r = 1
                    name = value
                    worksheet.write(0, cl, value)
            elif j == 2:
                if isinstance(value, float):
                    value = int(value)
                    worksheet.write(r, cl, value)
        r += 1

    chart = workbook.add_chart({'type': 'line'})
    # Configure the series of the chart from the dataframe data.
    for i in range(cl):
        col = i + 1
        chart.add_series({
            'name': ['Daily', 0, col],
            'categories': ['Daily', 1, 0, r, 0],
            'values': ['Daily', 1, col, r, col],
        })

    # Configure the chart axes.
    chart.set_x_axis({'name': 'Date'})
    chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})

    # Insert the chart into the worksheet.
    worksheet.insert_chart('D3', chart)

    workbook.close()


#select_stat2()


# class Stat_to_Excel:
#
#     workbook = Workbook('Total_Stat.xlsx')
#     db_file = 'list_of_games.db'
#
#     Players_Last_Day_Stat = '''with t1 as
#     ( select id, date, player1 player, player2 partner, pair1_avr_score pair_avr_score, pair1_Ea Ea, pair1_Sa Sa, pair1_Ra Ra, sign(pair1_Ra) win, sign(case when pair1_Ra > -1 and pair1_Ra < 1 then pair1_Ra end) tie_win from stat t
#     union all select id, date, player2 player, player1 partner, pair1_avr_score, pair1_Ea, pair1_Sa, pair1_Ra, sign(pair1_Ra) win, sign(case when pair1_Ra > -1 and pair1_Ra < 1 then pair1_Ra end) tie_win from stat t
#     union all select id, date, player3 player, player4 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra, sign(pair2_Ra) win, sign(case when pair1_Ra > -1 and pair1_Ra < 1 then pair1_Ra end) tie_win from stat t
#     union all select id, date, player4 player, player3 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra, sign(pair2_Ra) win, sign(case when pair1_Ra > -1 and pair1_Ra < 1 then pair1_Ra end) tie_win from stat t
#     )
#     select player                                                -- игрок
#          , sum(Ra) last_date_Ra                                  -- дельта счета за этот день
#          , count(case when win = 1 then 1 end) cnt_win           -- количество побед
#          , count(case when win = -1 then 1 end) cnt_lost         -- количество поражений
#          , count(case when tie_win = 1 then 1 end) cnt_tie_win   -- количество больше-меньше побед
#          , count(case when tie_win = -1 then 1 end) cnt_tie_lost -- количество больше-меньше поражений
#          , count(*) cnt_game                                     -- количество всего игр
#       from t1
#       where date = (select max(date) from stat)
#       group by player
#       order by sum(Ra) desc;'''
#
#     Players_Total_Stat = ''' with t1 as
#     ( select id, date, player1 player, player2 partner, pair1_avr_score pair_avr_score, pair1_Ea Ea, pair1_Sa Sa, pair1_Ra Ra from stat t
#     union all select id, date, player2 player, player1 partner, pair1_avr_score, pair1_Ea, pair1_Sa, pair1_Ra from stat t
#     union all select id, date, player3 player, player4 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
#     union all select id, date, player4 player, player3 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
#     ), t2 as
#     ( select t1.*
#            , rank() over (partition by player order by date desc) player_date_rank
#            , rank() over (order by date desc) date_rank
#         from t1
#     )
#     select player                                                -- игрок
#          , 500 + sum(Ra) score                                   -- текущий рейтинг
#          , sum(case when date_rank = 1 then Ra end) last_date_Ra -- дельту прироста за последнюю дату
#          , count(*) cnt_game                                     -- сколько игр было сыграно
#          , max(date) last_date                                   -- дата когда этот игрок играл последний раз
#       from t2
#       group by player
#       order by sum(Ra) desc;'''
#
#     def create_connection():
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :return: Connection object or None
#     """
#     db_file = self.db_file
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except Error as e:
#         print(e)
#
#     return conn

#     def export_report(self, report, header):
#
#         workbook = self.workbook
#         conn = create_connection()
#         c = conn.cursor()
#
#         worksheet = workbook.add_worksheet('Last-Day')
#         mysel = c.execute(Players_Last_Day_Stat)
#         header = ['Место', 'Игрок', 'Дельта', 'Победы', 'Поражения', 'Win(max/min)', 'Loss(max/min)', 'Всего Игр']
#         for idx, col in enumerate(header):
#             worksheet.write(0, idx, col)  # write the column name one time in a row
#
#         # write all data from SELECT. keep 1 row and 1 column NULL
#         for i, row in enumerate(mysel):
#             for j, value in enumerate(row):
#                 if isinstance(value, float):
#                     value = int(value)
#                 worksheet.write(i + 1, j + 1, value)
#
#         worksheet.write_column(1, 0, [i for i in range(1, len(c.execute(
#             Players_Last_Day_Stat).fetchall()) + 1)])  # make and insert column 1 with index
#
#         # here, we make both 1st column/row bold
#         bold_fmt = workbook.add_format({'bold': True})
#         worksheet.set_row(0, None, bold_fmt)
#         worksheet.set_column(0, 0, None, bold_fmt)