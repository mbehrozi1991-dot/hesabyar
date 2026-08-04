from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty


class ReportScreen(MDScreen):

    total_sales = StringProperty("۰ تومان")

    total_expenses = StringProperty("۰ تومان")

    total_profit = StringProperty("۰ تومان")


    def on_enter(self):

        self.load_reports()



    def load_reports(self):

        app = self.manager.app


        if hasattr(app, "db"):

            # دریافت اطلاعات واقعی از SQLite
            # در مرحله اتصال فعال می‌شود

            self.total_sales = "۰ تومان"

            self.total_expenses = "۰ تومان"

            self.total_profit = "۰ تومان"



    def refresh_reports(self):

        self.load_reports()
