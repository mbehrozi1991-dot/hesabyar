import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("hesabyar.db")
        self.create_tables()


    def create_tables(self):

        c = self.conn.cursor()

        c.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER,
            quantity INTEGER
        )
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone TEXT
        )
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            id INTEGER PRIMARY KEY,
            product TEXT,
            amount INTEGER
        )
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY,
            title TEXT,
            amount INTEGER
        )
        """)

        self.conn.commit()
