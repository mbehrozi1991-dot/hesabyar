from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from database import Database


db = Database()


class HomeScreen(Screen):
    pass


class ProductScreen(Screen):
    pass


class CustomerScreen(Screen):
    pass


class SaleScreen(Screen):
    pass


class ReportScreen(Screen):
    pass



class HesabyarApp(App):

    def build(self):

        Builder.load_file("hesabyar.kv")

        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ProductScreen(name="products"))
        sm.add_widget(CustomerScreen(name="customers"))
        sm.add_widget(SaleScreen(name="sales"))
        sm.add_widget(ReportScreen(name="reports"))

        return sm



if __name__ == "__main__":
    HesabyarApp().run()
# update
# test 36
