import sqlite3
from datetime import datetime


class Database:

    def __init__(self):

        self.conn = sqlite3.connect("hesabyar.db")

        self.create_tables()



    def create_tables(self):

        c = self.conn.cursor()


        c.execute("""
        CREATE TABLE IF NOT EXISTS stores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            address TEXT,
            created_at TEXT
        )
        """)



        c.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id INTEGER,
            name TEXT,
            barcode TEXT,
            buy_price INTEGER,
            sell_price INTEGER,
            quantity INTEGER,
            category TEXT
        )
        """)



        c.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id INTEGER,
            name TEXT,
            phone TEXT,
            address TEXT
        )
        """)



        c.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id INTEGER,
            customer_id INTEGER,
            total INTEGER,
            date TEXT
        )
        """)



        c.execute("""
        CREATE TABLE IF NOT EXISTS sale_items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            price INTEGER
        )
        """)



        c.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id INTEGER,
            title TEXT,
            amount INTEGER,
            date TEXT
        )
        """)


        self.conn.commit()



    # ---------- STORE ----------

    def add_store(self, name, phone="", address=""):

        c = self.conn.cursor()

        c.execute("""
        INSERT INTO stores
        (name,phone,address,created_at)
        VALUES (?,?,?,?)
        """,
        (
            name,
            phone,
            address,
            datetime.now().strftime("%Y-%m-%d")
        ))

        self.conn.commit()

        return c.lastrowid



    # ---------- PRODUCTS ----------

    def add_product(self, store_id, name, barcode,
                    buy_price, sell_price, quantity, category=""):

        c = self.conn.cursor()

        c.execute("""
        INSERT INTO products
        (store_id,name,barcode,buy_price,
        sell_price,quantity,category)
        VALUES (?,?,?,?,?,?,?)
        """,
        (
            store_id,
            name,
            barcode,
            buy_price,
            sell_price,
            quantity,
            category
        ))

        self.conn.commit()



    def get_products(self, store_id):

        c = self.conn.cursor()

        c.execute("""
        SELECT * FROM products
        WHERE store_id=?
        """,
        (store_id,))

        return c.fetchall()



    # ---------- CUSTOMERS ----------

    def add_customer(self, store_id, name, phone, address=""):

        c = self.conn.cursor()

        c.execute("""
        INSERT INTO customers
        (store_id,name,phone,address)
        VALUES (?,?,?,?)
        """,
        (
            store_id,
            name,
            phone,
            address
        ))

        self.conn.commit()



    def get_customers(self, store_id):

        c = self.conn.cursor()

        c.execute("""
        SELECT * FROM customers
        WHERE store_id=?
        """,
        (store_id,))

        return c.fetchall()



    # ---------- EXPENSES ----------

    def add_expense(self, store_id, title, amount):

        c = self.conn.cursor()

        c.execute("""
        INSERT INTO expenses
        (store_id,title,amount,date)
        VALUES (?,?,?,?)
        """,
        (
            store_id,
            title,
            amount,
            datetime.now().strftime("%Y-%m-%d")
        ))

        self.conn.commit()



    def get_expenses(self, store_id):

        c = self.conn.cursor()

        c.execute("""
        SELECT * FROM expenses
        WHERE store_id=?
        """,
        (store_id,))

        return c.fetchall()



    # ---------- REPORT ----------

    def get_total_expense(self, store_id):

        c = self.conn.cursor()

        c.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE store_id=?
        """,
        (store_id,))

        result = c.fetchone()[0]

        return result or 0
