from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty


class ExpenseScreen(MDScreen):

    expenses = ListProperty([])
    search_text = StringProperty("")

    def on_enter(self):
        self.load_expenses()

    def load_expenses(self):
        try:
            app = self.manager.app
            if hasattr(app, "db") and app.db:
                self.expenses = list(app.db.get_expenses(1))
        except Exception as e:
            print(f"Error loading expenses: {e}")

    def add_expense(self, title, amount):
        try:
            app = self.manager.app
            if hasattr(app, "db") and app.db:
                app.db.add_expense(1, title, int(amount))
                self.load_expenses()
        except Exception as e:
            print(f"Error adding expense: {e}")

    def delete_expense(self, expense_id):
        try:
            app = self.manager.app
            if hasattr(app, "db") and app.db and app.db.conn:
                c = app.db.conn.cursor()
                c.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
                app.db.conn.commit()
                self.load_expenses()
        except Exception as e:
            print(f"Error deleting expense: {e}")

    def search_expenses(self, text):
        self.search_text = text
        if text == "":
            self.load_expenses()
