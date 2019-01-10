import sqlite3


conn = sqlite3.connect('schedule.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS message;")
c.execute("""
CREATE TABLE message (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    content VARCHAR(150) NOT NULL,
    time TEXT NOT NULL
);
""")
c.execute("DROP TABLE IF EXISTS term;")
c.execute("""
CREATE TABLE term (
    id INTEGER NOT NULL PRIMARY KEY,
    start TEXT NOT NULL,
    end TEXT NOT NULL
);
""")
c.execute("DROP TABLE IF EXISTS lesson;")
c.execute("""
CREATE TABLE lesson (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    classroom TEXT NOT NULL,
    term INTEGER NOT NULL,
    week INTEGER NOT NULL,
    weekday INTEGER NOT NULL,
    time TEXT NOT NULL
);
""")
# c.execute("DROP TABLE IF EXISTS deadline;")
# c.execute("""
# CREATE TABLE deadline (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     time DATETIME NOT NULL,
#     title VARCHAR(30) NOT NULL,
#     detail VARCHAR(150) DEFAULT NULL,
#     create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     finish_time DATETIME DEFAULT NULL,
#     week_flag INTEGER DEFAULT NULL,
#     three_days_flag INTEGER DEFAULT NULL,
#     day_flag INTEGER DEFAULT NULL
# );
# """)
