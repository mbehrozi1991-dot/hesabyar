from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty


class ExpenseScreen(MDScreen):

    expenses = ListProperty([])

    search_text = StringProperty("")


    def on_enter(self):
        self.load_expenses()


    def load_expenses(self):

        app = self.manager.app

        self.expenses.clear()

        if hasattr(app, "db"):

            # دریافت هزینه‌ها از SQLite
            # در مرحله اتصال دیتابیس فعال می‌شود

            self.expenses = []



    def add_expense(self, title, amount):

        app = self.manager.app

        if hasattr(app, "db"):

            # ذخیره هزینه در دیتابیس

            pass


        self.load_expenses()



    def delete_expense(self, expense_id):

        app = self.manager.app

        if hasattr(app, "db"):

            # حذف هزینه

            pass


        self.load_expenses()



    def search_expenses(self, text):

        self.search_text = text
