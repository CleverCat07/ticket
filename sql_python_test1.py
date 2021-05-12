import sqlite3 as sql
from hashlib import sha256

con = sql.connect('test.db')
cur = con.cursor()
while True:
    print("1 - new \n2 - auth \n3 - exit")
    a = input()
    if a == "3":
        break
    nick = input("Введіть нік: ")
    key = input('Enter password: ')
    key = sha256(key.encode('utf-8')).hexdigest()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
           userid INT PRIMARY KEY,
           name TEXT,
           password TEXT);
        """)
    con.commit()
    if a == "1":
        cur.execute("""INSERT INTO users(name, password)
           VALUES( nick, key);""")
        con.commit()
    elif a == "2":
        cur.execute("SELECT * FROM users;")
        one_result = cur.fetchone()
        print(one_result)