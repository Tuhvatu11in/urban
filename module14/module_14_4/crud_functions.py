import sqlite3

def initiate_db(db_name='products.db'):
    """Создает таблицы Products и Users, если они ещё не созданы."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    """)

    conn.commit()
    conn.close()

def get_all_products(db_name='products.db'):
    """Возвращает все записи из таблицы Products."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()

    return products

def add_user(username, email, age, db_name='products.db'):
    """Добавляет пользователя в таблицу Users."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, 1000))
    conn.commit()
    conn.close()

def is_included(username, db_name='products.db'):
    """Проверяет, есть ли пользователь в таблице Users."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM Users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    return bool(result)
