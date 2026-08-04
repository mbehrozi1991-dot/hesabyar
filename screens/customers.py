from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty


class CustomerScreen(MDScreen):

    customers = ListProperty([])

    search_text = StringProperty("")


    def on_enter(self):
        self.load_customers()


    def load_customers(self):

        app = self.manager.app

        self.customers.clear()

        if hasattr(app, "db"):

            # در مرحله اتصال کامل دیتابیس
            # اطلاعات مشتریان از SQLite خوانده می‌شود

            self.customers = []



    def add_customer(self, name, phone, address):

        app = self.manager.app

        if hasattr(app, "db"):

            # ذخیره مشتری در دیتابیس

            pass

        self.load_customers()



    def delete_customer(self, customer_id):

        app = self.manager.app

        if hasattr(app, "db"):

            # حذف مشتری

            pass

        self.load_customers()



    def search_customers(self, text):

        self.search_text = text

        # جستجوی مشتری‌ها
