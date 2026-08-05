from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty


class CustomerScreen(MDScreen):

    customers = ListProperty([])
    search_text = StringProperty("")

    def on_enter(self):
        self.load_customers()

    def load_customers(self):
        try:
            app = self.manager.app
            if hasattr(app, "db") and app.db:
                self.customers = list(app.db.get_customers(1))
        except Exception as e:
            print(f"Error loading customers: {e}")

    def add_customer(self, name, phone, address=""):
        try:
            app = self.manager.app
            if hasattr(app, "db") and app.db:
                app.db.add_customer(1, name, phone, address)
                self.load_customers()
        except Exception as e:
            print(f"Error adding customer: {e}")

    def delete_customer(self, customer_id):
        try:
            app = self.manager.app
            if hasattr(app, "db") and app.db and app.db.conn:
                c = app.db.conn.cursor()
                c.execute("DELETE FROM customers WHERE id=?", (customer_id,))
                app.db.conn.commit()
                self.load_customers()
        except Exception as e:
            print(f"Error deleting customer: {e}")

    def search_customers(self, text):
        self.search_text = text
        if text == "":
            self.load_customers()
