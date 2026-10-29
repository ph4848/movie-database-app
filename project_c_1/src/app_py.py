import sqlite3

dbname = 'MoviesInfo.db'

def init_db():
    conn = sqlite3.connect(dbname)
    conn.close()
#----------------------------------------
#init_db()

def create_table():
    query = '''
        CREATE TABLE IF NOT EXISTS movies
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        country TEXT,
        year TEXT,
        imdb_rate REAL
        )
                '''
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
#----------------------------------------
create_table()

def insert_record(title, country, year, imdb_rate):
    query = '''
                INSERT INTO movies(title, country, year, imdb_rate)
                VALUES(?, ?, ?, ?)
                '''
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(query, (title, country, year, imdb_rate))
    conn.commit()
    conn.close()
#----------------------------------------
#insert_record("Odyssey", "America", "2026", 8.7)
#insert_record("Openheimer", "America", "2024", 8.7)
#insert_record("KillBill", "Germany", "2004", 7.9)
#----------------------------------------
def select_all_records():
    query = 'SELECT * FROM movies'
    query_2 = 'SELECT title, country FROM movies'
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    rows = cursor.execute(query_2).fetchall()
    conn.close()
    return rows
#----------------------------------------
#print(select_all_records())

def select_record_by_id(id):
    query = 'SELECT * FROM movies WHERE id = ?'
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    rows = cursor.execute(query, (id,)).fetchone()
    conn.close()
    return rows
#----------------------------------------
#print(select_record_by_id(3))

def select_record_by_name(title):
    query = 'SELECT * FROM movies WHERE title = ?'
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    rows = cursor.execute(query, (title,)).fetchone()
    conn.close()
    return rows
#----------------------------------------
#print(select_record_by_name("Odyssey"))

def delete_record_by_id(id):
    query = '''DELETE FROM movies WHERE id = ?'''
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()   
#----------------------------------------
#delete_record_by_id(1)

def update_record_by_id(id, imdb_rate, year):
    query = '''UPDATE movies SET imdb_rate = ? , year = ? WHERE id = ?'''
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(query, (imdb_rate, year, id))
    conn.commit()
    conn.close()   
#----------------------------------------
#update_record_by_id(2, 8.2, "2025")