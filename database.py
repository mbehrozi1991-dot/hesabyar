import sqlite3
from datetime import datetime


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("hesabyar.db")
        self.create_tables()


    def create_tables(self):

        cursor = self.conn.cursor()

        # فروشگاه‌ها
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS stores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            address TEXT,
            created_at TEXT
        )
        """)

        # کاربران (برای توسعه آینده)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
        """)

        # کالاها
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id INTEGER,
            name TEXT NOT NULL,
            barcode TEXT,
            buy_price INTEGER DEFAULT 0,
            sell_price INTEGER DEFAULT 0,
            quantity INTEGER DEFAULT 0,
            category TEXT,
            FOREIGN KEY(store_id) REFERENCES stores(id)
        )
        """)

        # مشتریان
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id INTEGER,
            name TEXT NOT NULL,
            phone TEXT,
            address TEXT,
            FOREIGN KEY(store_id) REFERENCES stores(id)
        )
        """)

        # فاکتور فروش
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id INTEGER,
            customer_id INTEGER,
            total INTEGER DEFAULT 0,
            date TEXT,
            FOREIGN KEY(store_id) REFERENCES stores(id),
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
        """)

        # اقلام داخل فاکتور
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sale_items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            price INTEGER,
            FOREIGN KEY(sale_id) REFERENCES sales(id),
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
        """)

        # هزینه‌ها
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id INTEGER,
            title TEXT,
            amount INTEGER,
            date TEXT,
            FOREIGN KEY(store_id) REFERENCES stores(id)
        )
        """)

        # تنظیمات
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id INTEGER,
            key TEXT,
            value TEXT,
            FOREIGN KEY(store_id) REFERENCES stores(id)
        )
        """)

        self.conn.commit()


    def add_store(self, name, phone="", address=""):

        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO stores(name, phone, address, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            name,
            phone,
            address,
            datetime.now().strftime("%Y-%m-%d")
        ))

        self.conn.commit()

        return cursor.lastrowid
