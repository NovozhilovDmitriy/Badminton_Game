import sqlite3
from sqlite3 import Error

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

    Players_Total_Stat = ''' with t1 as
    ( select id, date, player1 player, player2 partner, pair1_avr_score pair_avr_score, pair1_Ea Ea, pair1_Sa Sa, pair1_Ra Ra from stat t
    union all select id, date, player2 player, player1 partner, pair1_avr_score, pair1_Ea, pair1_Sa, pair1_Ra from stat t
    union all select id, date, player3 player, player4 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
    union all select id, date, player4 player, player3 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
    ), t2 as
    ( select t1.*
           , row_number() over (partition by player order by date desc, id desc) game_rank
           , rank() over (partition by player order by date desc) date_rank
        from t1
    )
    select player
         , 500 + sum(Ra) score -- текущий рейтинг
         , sum(case when date_rank = 1 then Ra end) last_date_Ra -- дельту прироста за последнюю дату
         , count(*) cnt_game -- сколько игр было сыграно
      from t2
      group by player
      order by sum(Ra) desc;'''

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

    Players_daily_stat = '''with t1 as
    ( select id, date, player1 player, player2 partner, pair1_avr_score pair_avr_score, pair1_Ea Ea, pair1_Sa Sa, pair1_Ra Ra from stat t
    union all select id, date, player2 player, player1 partner, pair1_avr_score, pair1_Ea, pair1_Sa, pair1_Ra from stat t
    union all select id, date, player3 player, player4 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
    union all select id, date, player4 player, player3 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
    )
    select player
         , date
         , 500 + sum(sum(Ra)) over (partition by player order by date) score -- текущий рейтинг
         , sum(count(*)) over (partition by player order by date) cnt_game -- сколько игр было сыграно
      from t1
      group by player, date
      order by player, date;'''

    Players_daily2_stat = '''with d as
( select distinct date from stat
), pl as
( select distinct player from (select player1 player from stat union all select player2 from stat union all select player3 from stat union all select player4 from stat)
), t1 as
( select id, date, player1 player, player2 partner, pair1_avr_score pair_avr_score, pair1_Ea Ea, pair1_Sa Sa, pair1_Ra Ra from stat t
union all select id, date, player2 player, player1 partner, pair1_avr_score, pair1_Ea, pair1_Sa, pair1_Ra from stat t
union all select id, date, player3 player, player4 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
union all select id, date, player4 player, player3 partner, pair2_avr_score, pair2_Ea, pair2_Sa, pair2_Ra from stat t
) 
select pl.player
     , d.date
     , case when count(Ra) <> 0 then 500 + coalesce(sum(sum(Ra)) over (partition by pl.player order by d.date), 0) end score -- текущий рейтинг
  from d cross join pl
       left outer join t1 on t1.date = d.date and t1.player = pl.player
  group by pl.player, d.date
  order by pl.player, d.date;'''

    from xlsxwriter.workbook import Workbook
    workbook = Workbook('Total_Stat.xlsx')
    worksheet = workbook.add_worksheet('Total')

    conn = create_connection()
    c=conn.cursor()
    mysel=c.execute(Players_Total_Stat)
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i, j, value)

    worksheet = workbook.add_worksheet('Pair-Win')
    mysel=c.execute(Players_win_pair_stat)
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i, j, value)

    worksheet = workbook.add_worksheet('Opponent-Win')
    mysel=c.execute(Players_win_opponent_stat)
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i, j, value)

    worksheet = workbook.add_worksheet('Daily')
    mysel=c.execute(Players_daily_stat)
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i, j, value)

    worksheet = workbook.add_worksheet('Daily2')
    mysel=c.execute(Players_daily2_stat)
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i, j, value)
    workbook.close()
