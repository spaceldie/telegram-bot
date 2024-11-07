import sqlite3

# Подключение к базе данных или создание файла .db
conn = sqlite3.connect("game_bot.db")
cursor = conn.cursor()

# Создание таблицы для пользователей
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    level TEXT,
                    experience INTEGER
                )''')
conn.commit()

# Функция для добавления нового пользователя
def add_user(user_id, username):
    cursor.execute("INSERT OR IGNORE INTO users (user_id, username, level, experience) VALUES (?, ?, ?, ?)",
                   (user_id, username, 'Средневековье', 0))
    conn.commit()

# Функция для обновления уровня или опыта
def update_user(user_id, level=None, experience=None):
    if level:
        cursor.execute("UPDATE users SET level = ? WHERE user_id = ?", (level, user_id))
    if experience is not None:
        cursor.execute("UPDATE users SET experience = ? WHERE user_id = ?", (experience, user_id))
    conn.commit()

# Функция для получения данных пользователя
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return cursor.fetchone()