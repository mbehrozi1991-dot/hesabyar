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

            # در مرحله اتصال کامل دیتابیس
            # این قسمت با اطلاعات واقعی پر می‌شود

            self.store_name = "فروشگاه من"

            self.total_inventory = self.format_price(0)
            self.today_sales = self.format_price(0)
            self.today_expenses = self.format_price(0)
            self.monthly_profit = self.format_price(0)

            self.product_count = 0
            self.customer_count = 0



    def format_price(self, price):

        return "{:,} تومان".format(price)


    def refresh_dashboard(self):

        self.load_dashboard()


    def get_date(self):

        return datetime.now().strftime("%Y/%m/%d")
