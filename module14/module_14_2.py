import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_records = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]

average_balance = total_balance / total_records

print(f"Общее количество записей: {total_records}")
print(f"Сумма всех балансов: {total_balance}")
print(f"Средний баланс: {average_balance}")

conn.commit()
conn.close()
