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
c.execute("DROP TABLE IF EXISTS plan;")
c.execute("""
CREATE TABLE plan (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    time DATETIME,
    detail TEXT,
    create_time DATETIME NOT NULL DEFAULT (datetime('now','localtime')),
    flag INTEGER NOT NULL
);
""")
