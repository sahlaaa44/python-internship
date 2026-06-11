import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    mark REAL,
    grade TEXT
)
""")

cursor.execute("DELETE FROM students")

students = [
    ("john", 98),
    ("ali", 56),
    ("alice", 89),
    ("soya", 90),
    ("zera", 78)
]

for name, mark in students:
    cursor.execute(
        "INSERT INTO students (name, mark) VALUES (?, ?)",
        (name, mark)
    )

conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)
conn.close()
