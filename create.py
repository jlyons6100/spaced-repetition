import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS questions
             (ques text PRIMARY KEY, ans text)''')

while True:
    quit = ''
    while quit != 'n' and quit != 'y':
        quit = input("Add question? (y/n) ")
    if quit == 'n':
        break
    ques = input("Ques?")
    ans = input("Ans?")
    # Insert data

    sql = "INSERT OR IGNORE INTO questions(ques,ans) VALUES(?,?)"
    c.execute(sql, (ques,ans))

# Save changes

conn.commit()

conn.close()
