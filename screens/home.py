from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, NumericProperty
from datetime import datetime


class HomeScreen(MDScreen):

    store_name = StringProperty("فروشگاه من")

    total_inventory = StringProperty("۰ تومان")
    today_sales = StringProperty("۰ تومان")
    today_expenses = StringProperty("۰ تومان")
    monthly_profit = StringProperty("۰ تومان")

    product_count = NumericProperty(0)
    customer_count = NumericProperty(0)


    def on_enter(self):
        self.load_dashboard()


    def load_dashboard(self):

        app = self.manager.app

        if hasattr(app, "db"):

            # حساب موجودی انبار
            total_inventory = self.calculate_total_inventory()

            # حساب فروش امروز
            today_sales = self.calculate_today_sales()

            # حساب هزینه امروز
            today_expenses = app.db.get_total_expense(1)

            # حساب سود ماهانه
            monthly_profit = self.calculate_monthly_profit()

            self.store_name = "فروشگاه من"

            self.total_inventory = self.format_price(total_inventory)
            self.today_sales = self.format_price(today_sales)
            self.today_expenses = self.format_price(today_expenses)
            self.monthly_profit = self.format_price(monthly_profit)

            # تعداد کالا و مشتری
            products = app.db.get_products(1)
            customers = app.db.get_customers(1)

            self.product_count = len(products)
            self.customer_count = len(customers)



    def calculate_total_inventory(self):
        """محاسبه کل موجودی انبار"""
        app = self.manager.app
        total = 0

        if hasattr(app, "db"):
            products = app.db.get_products(1)
            for product in products:
                # product = (id, store_id, name, barcode, buy_price, sell_price, quantity, category)
                quantity = product[6] if len(product) > 6 else 0
                sell_price = product[5] if len(product) > 5 else 0
                total += quantity * sell_price

        return total



    def calculate_today_sales(self):
        """محاسبه فروش امروز"""
        app = self.manager.app
        today = datetime.now().strftime("%Y-%m-%d")
        total = 0

        if hasattr(app, "db"):
            c = app.db.conn.cursor()
            c.execute("""
            SELECT SUM(total) FROM sales
            WHERE store_id=? AND date=?
            """, (1, today))

            result = c.fetchone()[0]
            total = result if result else 0

        return total



    def calculate_monthly_profit(self):
        """محاسبه سود ماهانه"""
        app = self.manager.app
        total_sales = 0
        total_costs = 0

        if hasattr(app, "db"):
            # کل فروش ماه
            c = app.db.conn.cursor()
            c.execute("""
            SELECT SUM(total) FROM sales
            WHERE store_id=?
            """, (1,))

            result = c.fetchone()[0]
            total_sales = result if result else 0

            # کل هزینه‌ها
            total_costs = app.db.get_total_expense(1)

        profit = total_sales - total_costs
        return profit if profit > 0 else 0


    def format_price(self, price):
        return "{:,} تومان".format(price)


    def refresh_dashboard(self):
        self.load_dashboard()


    def get_date(self):
        return datetime.now().strftime("%Y/%m/%d")
