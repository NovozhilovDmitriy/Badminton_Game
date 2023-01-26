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
    #cursor.execute(players_score)
    sqlite_connection.commit()
    record = cursor.fetchall()
    print(record)
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
    record = cursor.fetchall()
    print(record)
    cursor.close()

def drop_table_stat():
    # Connecting to sqlite
    conn = sqlite3.connect('list_of_games.db')

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Doping EMPLOYEE table if already exists
    cursor.execute("DROP TABLE IF EXISTS stat")
    #print("Table dropped... ")

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()

#create_table()
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def insert_game(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO games(date,player1,player2,player3,player4,score1,score2)
              VALUES(?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def insert_stat(task):
    database = 'list_of_games.db'

    # create a database connection
    conn = create_connection(database)

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

def insert_player(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO players(name,score,daily_score)
              VALUES(?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def check_date(date):
    database = 'list_of_games.db'

    # create a database connection
    conn = create_connection(database)
    sql = ''' select date from games where date = (?) '''
    cur = conn.cursor()
    cur.execute(sql, (date,))
    result = cur.fetchall()
    if len(result) == 0:
        return True
    else:
        return False

def table_date_list():
    database = 'list_of_games.db'

    # create a database connection
    conn = create_connection(database)
    sql = ''' select distinct date from games order by date asc; '''
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return list(result)

def export_one_day_games(date):
    database = 'list_of_games.db'
    # create a database connection
    conn = create_connection(database)
    sql = ''' select player1,player2,player3,player4,score1,score2 from games where date = ? order by id asc ;'''
    conn.row_factory = sqlite3.Row
    values = conn.execute(sql, (date,)).fetchall()
    list = []
    for item in values:
        list.append({k: item[k] for k in item.keys()})
    return list

# queue = table_date_list()
# for i in queue:
#     Players_Dict = export_one_day_games(i)

def insert_games(games):
    database = 'list_of_games.db'

    # create a database connection
    conn = create_connection(database)
    with conn:
        # tasks
        task_1 = games

        # create tasks
        insert_game(conn, task_1)
