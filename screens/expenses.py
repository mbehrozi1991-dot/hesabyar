from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty


class ExpenseScreen(MDScreen):

    expenses = ListProperty([])

    search_text = StringProperty("")


    def on_enter(self):

        self.load_expenses()



    def load_expenses(self):

        app = self.manager.app

        self.expenses = []


        if hasattr(app, "db"):

            data = app.db.get_expenses(1)


            for item in data:

                self.expenses.append(item)




    def add_expense(self, title, amount):

        app = self.manager.app


        if hasattr(app, "db"):

            app.db.add_expense(

                1,

                title,

                int(amount)

            )


        self.load_expenses()




    def delete_expense(self, expense_id):

        # حذف هزینه در مرحله بعد اضافه می‌شود

        self.load_expenses()




    def search_expenses(self, text):

        self.search_text = text
