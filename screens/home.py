from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, NumericProperty


class HomeScreen(MDScreen):

    store_name = StringProperty("فروشگاه من")

    total_inventory = StringProperty("۰ تومان")
    today_sales = StringProperty("۰ تومان")
    today_expenses = StringProperty("۰ تومان")
    monthly_profit = StringProperty("۰ تومان")

    product_count = NumericProperty(0)
    customer_count = NumericProperty(0)


    def on_enter(self):
        self.refresh_dashboard()


    def refresh_dashboard(self):
        try:
            app = self.manager.app
            if not hasattr(app, "db") or app.db is None:
                return

            self.product_count = len(app.db.get_products(1))
            self.customer_count = len(app.db.get_customers(1))
            self.total_inventory = "۰ تومان"
            self.today_sales = "۰ تومان"
            self.today_expenses = "۰ تومان"
            self.monthly_profit = "۰ تومان"
        except Exception as e:
            print(f"Error loading dashboard: {e}")
