import sqlite3
import random
all_data = []

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("SELECT * FROM questions")
rows = c.fetchall()

while True:
    cur = rows[random.randint(0, len(rows)-1)]
    print(cur[0])
    input("")
    print(cur[1])
    input("")
conn.close()
