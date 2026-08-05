from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty
from datetime import datetime


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

        app = self.manager.app

        if hasattr(app, "db"):

            c = app.db.conn.cursor()

            c.execute("DELETE FROM expenses WHERE id=?", (expense_id,))

            app.db.conn.commit()

        self.load_expenses()


    def edit_expense(self, expense_id, title, amount):

        app = self.manager.app

        if hasattr(app, "db"):

            c = app.db.conn.cursor()

            c.execute("""
            UPDATE expenses
            SET title=?, amount=?
            WHERE id=?
            """, (title, int(amount), expense_id))

            app.db.conn.commit()

        self.load_expenses()


    def search_expenses(self, text):

        self.search_text = text

        if text == "":
            self.load_expenses()
            return

        app = self.manager.app
        filtered_expenses = []

        if hasattr(app, "db"):

            c = app.db.conn.cursor()

            c.execute("""
            SELECT * FROM expenses
            WHERE store_id=1 AND title LIKE ?
            """, (f"%{text}%",))

            for item in c.fetchall():
                filtered_expenses.append(item)

        self.expenses = filtered_expenses
