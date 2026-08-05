from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from datetime import datetime


class ReportScreen(MDScreen):

    total_sales = StringProperty("۰ تومان")

    total_expenses = StringProperty("۰ تومان")

    total_profit = StringProperty("۰ تومان")

    total_products = StringProperty("۰ عدد")

    total_customers = StringProperty("۰ نفر")


    def on_enter(self):

        self.load_reports()



    def load_reports(self):

        app = self.manager.app


        if hasattr(app, "db"):

            # کل فروش
            total_sales = self.calculate_total_sales()

            # کل هزینه‌ها
            total_expenses = app.db.get_total_expense(1)

            # کل سود
            total_profit = total_sales - total_expenses

            # تعداد کالاها
            products = app.db.get_products(1)
            total_products = len(products)

            # تعداد مشتریان
            customers = app.db.get_customers(1)
            total_customers = len(customers)

            self.total_sales = self.format_price(total_sales)
            self.total_expenses = self.format_price(total_expenses)
            self.total_profit = self.format_price(total_profit if total_profit > 0 else 0)
            self.total_products = f"{total_products} عدد"
            self.total_customers = f"{total_customers} نفر"


    def calculate_total_sales(self):
        """محاسبه کل فروش"""
        app = self.manager.app
        total = 0

        if hasattr(app, "db"):
            c = app.db.conn.cursor()
            c.execute("""
            SELECT SUM(total) FROM sales
            WHERE store_id=1
            """)

            result = c.fetchone()[0]
            total = result if result else 0

        return total


    def format_price(self, price):
        return "{:,} تومان".format(price)


    def refresh_reports(self):

        self.load_reports()
