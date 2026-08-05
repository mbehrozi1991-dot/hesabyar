from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, NumericProperty, StringProperty


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
        try:
            item = {
                "product_id": product_id,
                "product_name": product_name,
                "quantity": int(quantity),
                "price": int(price)
            }
            self.cart.append(item)
            self.calculate_total()
        except Exception as e:
            print(f"Error adding to cart: {e}")

    def calculate_total(self):
        total = 0
        for item in self.cart:
            total += item.get("price", 0) * item.get("quantity", 0)
        self.total_price = total

    def save_sale(self, customer_id=None):
        try:
            app = self.manager.app
            if hasattr(app, "db") and app.db and app.db.conn and len(self.cart) > 0:
                c = app.db.conn.cursor()
                c.execute("""
                INSERT INTO sales (store_id, customer_id, total, date)
                VALUES (?, ?, ?, ?)
                """, (1, customer_id, self.total_price, "2026-08-05"))
                app.db.conn.commit()
            self.reset_sale()
        except Exception as e:
            print(f"Error saving sale: {e}")

    def remove_item(self, index):
        try:
            if index < len(self.cart):
                self.cart.pop(index)
                self.calculate_total()
        except Exception as e:
            print(f"Error removing item: {e}")
