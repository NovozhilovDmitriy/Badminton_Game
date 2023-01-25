import sqlite3
from sqlite3 import Error

def create_table():
    sqlite_connection = sqlite3.connect('list_of_games.db')
    games_table = '''CREATE TABLE games (
                    id INTEGER PRIMARY KEY,
                    date datetime NOT NULL,
                    player1 TEXT NOT NULL,
                    player2 TEXT NOT NULL,
                    player3 TEXT NOT NULL,
                    player4 TEXT NOT NULL,
                    score1 INTEGER NOT NULL,
                    score2 INTEGER NOT NULL);'''
    cursor = sqlite_connection.cursor()
    cursor.execute(games_table)
    sqlite_connection.commit()
    cursor.execute("select * from games;")
    record = cursor.fetchall()
    print(record)
    cursor.close()


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


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO games(date,player1,player2,player3,player4,score1,score2)
              VALUES('01-01-2023',?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def insert_games(games):
    database = 'list_of_games.db'

    # create a database connection
    conn = create_connection(database)
    with conn:
        # tasks
        task_1 = games

        # create tasks
        create_task(conn, task_1)

