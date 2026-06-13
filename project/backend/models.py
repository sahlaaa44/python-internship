import sqlite3

conn = sqlite3.connect("task_manager.db",
                       check_same_thread= False
                       )
cursor = conn.cursor()

def craete_table():
    cursor.execu("""
                 CRAETE TABLE IF NOT EXISTS users(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE NOT NULL,
                 email TEXT UNIQUE NOT NULL,
                 password TEXT NOT NULL
    )
    """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tasks(
                   id INTEGER PRIMARY KEY AUTOIMCREMENT,
                   username TEXT  NOT NULL,
                   title NEXT NOT NULL,
                   description TEXT,
                   priority TEXT,
                   due_date TEXT,
                   completed INTEGER DEFAULT 0
                   )
                   """)
    
    conn.commit()

    craete_table()