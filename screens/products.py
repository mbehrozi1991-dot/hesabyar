from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty


class ProductScreen(MDScreen):

    products = ListProperty([])

    search_text = StringProperty("")


    def on_enter(self):
        self.load_products()


    def load_products(self):

        app = self.manager.app

        self.products.clear()

        if hasattr(app, "db"):

            # اتصال واقعی به دیتابیس در مرحله بعد

            self.products = []


    def add_product(self, name, barcode, buy_price, sell_price, quantity):

        app = self.manager.app

        if hasattr(app, "db"):

            # ذخیره کالا در دیتابیس

            pass

        self.load_products()



    def delete_product(self, product_id):

        app = self.manager.app

        if hasattr(app, "db"):

            # حذف کالا از دیتابیس

            pass

        self.load_products()



    def search_products(self, text):

        self.search_text = text

        # جستجوی کالاها در نسخه دیتابیس فعال می‌شود
