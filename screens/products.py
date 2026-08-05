from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty
import sqlite3


class ProductScreen(MDScreen):

    products = ListProperty([])

    search_text = StringProperty("")


    def on_enter(self):

        self.load_products()



    def load_products(self):

        app = self.manager.app

        self.products = []

        if hasattr(app, "db"):

            # فعلا فروشگاه شماره 1
            data = app.db.get_products(1)

            for item in data:

                self.products.append(item)



    def add_product(self,
                    name,
                    barcode,
                    buy_price,
                    sell_price,
                    quantity):


        app = self.manager.app


        if hasattr(app, "db"):


            app.db.add_product(

                1,

                name,

                barcode,

                int(buy_price),

                int(sell_price),

                int(quantity),

                ""

            )


        self.load_products()



    def delete_product(self, product_id):

        app = self.manager.app

        if hasattr(app, "db"):

            c = app.db.conn.cursor()

            c.execute("DELETE FROM products WHERE id=?", (product_id,))

            app.db.conn.commit()

        self.load_products()


    def edit_product(self, product_id, name, barcode, buy_price, sell_price, quantity):

        app = self.manager.app

        if hasattr(app, "db"):

            c = app.db.conn.cursor()

            c.execute("""
            UPDATE products
            SET name=?, barcode=?, buy_price=?, sell_price=?, quantity=?
            WHERE id=?
            """, (name, barcode, int(buy_price), int(sell_price), int(quantity), product_id))

            app.db.conn.commit()

        self.load_products()


    def search_products(self, text):

        self.search_text = text

        if text == "":
            self.load_products()
            return

        app = self.manager.app
        filtered_products = []

        if hasattr(app, "db"):

            c = app.db.conn.cursor()

            c.execute("""
            SELECT * FROM products
            WHERE store_id=1 AND name LIKE ?
            """, (f"%{text}%",))

            for item in c.fetchall():
                filtered_products.append(item)

        self.products = filtered_products
