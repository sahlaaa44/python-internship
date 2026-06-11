from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Database connection
conn = sqlite3.connect("app.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
""")
conn.commit()

# POST: Create task
@app.post("/tasks")
def create_task(task: dict):
    cursor.execute(
        "INSERT INTO tasks(title) VALUES(?)",
        (task["title"],)
    )
    conn.commit()

    return {
        "id": cursor.lastrowid,
        "title": task["title"]
    }

# GET: View all tasks
@app.get("/tasks")
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    tasks = []
    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1]
        })

    return tasks