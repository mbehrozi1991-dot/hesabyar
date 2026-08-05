from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty


class ProductScreen(MDScreen):

    products = ListProperty([])
    search_text = StringProperty("")

    def on_enter(self):
        self.load_products()

    def load_products(self):
        try:
            app = self.manager.app
            if hasattr(app, "db") and app.db:
                self.products = list(app.db.get_products(1))
        except Exception as e:
            print(f"Error loading products: {e}")

    def add_product(self, name, barcode, buy_price, sell_price, quantity):
        try:
            app = self.manager.app
            if hasattr(app, "db") and app.db:
                app.db.add_product(1, name, barcode, int(buy_price), int(sell_price), int(quantity), "")
                self.load_products()
        except Exception as e:
            print(f"Error adding product: {e}")

    def delete_product(self, product_id):
        try:
            app = self.manager.app
            if hasattr(app, "db") and app.db and app.db.conn:
                c = app.db.conn.cursor()
                c.execute("DELETE FROM products WHERE id=?", (product_id,))
                app.db.conn.commit()
                self.load_products()
        except Exception as e:
            print(f"Error deleting product: {e}")

    def search_products(self, text):
        self.search_text = text
        if text == "":
            self.load_products()
