from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from database import Database

from screens.home import HomeScreen
from screens.products import ProductScreen
from screens.customers import CustomerScreen
from screens.sales import SaleScreen
from screens.reports import ReportScreen
from screens.expenses import ExpenseScreen


class HesabyarApp(MDApp):

    def build(self):

        self.title = "حساب‌یار"

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        self.db = Database()

        Builder.load_file("hesabyar.kv")

        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ProductScreen(name="products"))
        sm.add_widget(CustomerScreen(name="customers"))
        sm.add_widget(SaleScreen(name="sales"))
        sm.add_widget(ReportScreen(name="reports"))
        sm.add_widget(ExpenseScreen(name="expenses"))

        return sm


if __name__ == "__main__":
    HesabyarApp().run()
