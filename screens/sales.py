from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty, NumericProperty
from datetime import datetime


class SaleScreen(MDScreen):

    cart = ListProperty([])

    customer_name = StringProperty("")

    total_price = NumericProperty(0)


    def on_enter(self):
        self.reset_sale()


    def reset_sale(self):

        self.cart = []
        self.customer_name = ""
        self.total_price = 0



    def add_to_cart(self, product_id, product_name, quantity, price):

        item = {
            "product_id": product_id,
            "product_name": product_name,
            "quantity": int(quantity),
            "price": int(price)
        }

        self.cart.append(item)

        self.calculate_total()



    def calculate_total(self):

        total = 0

        for item in self.cart:

            total += item.get("price", 0) * item.get("quantity", 0)


        self.total_price = total



    def save_sale(self, customer_id=None):

        app = self.manager.app

        if hasattr(app, "db") and len(self.cart) > 0:

            c = app.db.conn.cursor()

            # ثبت فاکتور فروش
            c.execute("""
            INSERT INTO sales (store_id, customer_id, total, date)
            VALUES (?, ?, ?, ?)
            """, (1, customer_id, self.total_price, datetime.now().strftime("%Y-%m-%d")))

            sale_id = c.lastrowid

            # ثبت اقلام فروش
            for item in self.cart:

                c.execute("""
                INSERT INTO sale_items (sale_id, product_id, quantity, price)
                VALUES (?, ?, ?, ?)
                """, (sale_id, item["product_id"], item["quantity"], item["price"]))

                # بروزرسانی تعداد کالا
                c.execute("""
                UPDATE products
                SET quantity = quantity - ?
                WHERE id=?
                """, (item["quantity"], item["product_id"]))

            app.db.conn.commit()


        self.reset_sale()



    def remove_item(self, index):

        if index < len(self.cart):

            self.cart.pop(index)

            self.calculate_total()
