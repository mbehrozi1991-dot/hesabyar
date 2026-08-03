import sqlite3


class Database:

    def __init__(self):

        self.conn = sqlite3.connect("hesabyar.db")

        self.cursor = self.conn.cursor()

        self.create_tables()



    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            quantity INTEGER
        )
        """)


        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT
        )
        """)


        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT,
            product TEXT,
            quantity INTEGER,
            total INTEGER
        )
        """)


        self.conn.commit()



    # محصولات

    def add_product(self, name, price, quantity):

        self.cursor.execute(
            """
            INSERT INTO products(name,price,quantity)
            VALUES(?,?,?)
            """,
            (name, price, quantity)
        )

        self.conn.commit()



    def get_products(self):

        self.cursor.execute(
            "SELECT * FROM products"
        )

        return self.cursor.fetchall()



    # مشتری‌ها

    def add_customer(self, name, phone):

        self.cursor.execute(
            """
            INSERT INTO customers(name,phone)
            VALUES(?,?)
            """,
            (name, phone)
        )

        self.conn.commit()



    def get_customers(self):

        self.cursor.execute(
            "SELECT * FROM customers"
        )

        return self.cursor.fetchall()



    # فروش

    def add_sale(self, customer, product, quantity, total):

        self.cursor.execute(
            """
            INSERT INTO sales(customer,product,quantity,total)
            VALUES(?,?,?,?)
            """,
            (
                customer,
                product,
                quantity,
                total
            )
        )

        self.cursor.commit()



    def get_sales(self):

        self.cursor.execute(
            "SELECT * FROM sales"
        )

        return self.cursor.fetchall()
