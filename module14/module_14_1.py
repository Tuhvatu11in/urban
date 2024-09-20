import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

for i in range(1, 11):
    cursor.execute(
        "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
        (f"User{i}", f"example{i}@gmail.com", i * 10, 1000)
    )

for i in range(1, 11, 2):
    cursor.execute(
        "UPDATE Users SET balance = 500 WHERE id = ?", (i,)
    )

for i in range(1, 11, 3):
    cursor.execute(
        "DELETE FROM Users WHERE id = ?", (i,)
    )

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()

for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
