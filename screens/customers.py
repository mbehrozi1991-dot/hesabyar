from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty


class CustomerScreen(MDScreen):

    customers = ListProperty([])

    search_text = StringProperty("")


    def on_enter(self):

        self.load_customers()



    def load_customers(self):

        app = self.manager.app

        self.customers = []


        if hasattr(app, "db"):

            data = app.db.get_customers(1)


            for item in data:

                self.customers.append(item)




    def add_customer(self, name, phone, address=""):

        app = self.manager.app


        if hasattr(app, "db"):


            app.db.add_customer(

                1,

                name,

                phone,

                address

            )


        self.load_customers()




    def delete_customer(self, customer_id):

        # حذف مشتری در مرحله بعد اضافه می‌شود

        self.load_customers()




    def search_customers(self, text):

        self.search_text = text
