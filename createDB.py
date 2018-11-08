import sqlite3


conn = sqlite3.connect('schedule.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS message;")
c.execute("""
CREATE TABLE message (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    content VARCHAR(150) NOT NULL,
    time DATETIME NOT NULL,
    read_flag INTEGER NOT NULL DEFAULT 0
);
""")
c.execute("DROP TABLE IF EXISTS deadline;")
c.execute("""
CREATE TABLE deadline (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    time DATETIME NOT NULL,
    title VARCHAR(30) NOT NULL,
    detail VARCHAR(150) DEFAULT NULL,
    create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finish_time DATETIME DEFAULT NULL,
    week_flag INTEGER DEFAULT NULL,
    three_days_flag INTEGER DEFAULT NULL,
    day_flag INTEGER DEFAULT NULL
);
""")
