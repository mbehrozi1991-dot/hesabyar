from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty


class ReportScreen(MDScreen):

    total_sales = StringProperty("۰ تومان")
    total_expenses = StringProperty("۰ تومان")
    total_profit = StringProperty("۰ تومان")
    total_products = StringProperty("۰ عدد")
    total_customers = StringProperty("۰ نفر")

    def on_enter(self):
        self.refresh_reports()

    def refresh_reports(self):
        try:
            app = self.manager.app
            if not hasattr(app, "db") or app.db is None:
                return

            products = app.db.get_products(1)
            customers = app.db.get_customers(1)

            self.total_products = f"{len(products)} عدد"
            self.total_customers = f"{len(customers)} نفر"
            self.total_sales = "۰ تومان"
            self.total_expenses = "۰ تومان"
            self.total_profit = "۰ تومان"
        except Exception as e:
            print(f"Error loading reports: {e}")
