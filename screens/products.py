from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty


class ProductScreen(MDScreen):

    products = ListProperty([])

    search_text = StringProperty("")


    def on_enter(self):

        self.load_products()



    def load_products(self):

        app = self.manager.app

        self.products = []

        if hasattr(app, "db"):

            # فعلا فروشگاه شماره 1
            data = app.db.get_products(1)

            for item in data:

                self.products.append(item)



    def add_product(self,
                    name,
                    barcode,
                    buy_price,
                    sell_price,
                    quantity):


        app = self.manager.app


        if hasattr(app, "db"):


            app.db.add_product(

                1,

                name,

                barcode,

                int(buy_price),

                int(sell_price),

                int(quantity),

                ""

            )


        self.load_products()



    def delete_product(self, product_id):

        # حذف در مرحله بعد اضافه می‌شود

        self.load_products()



    def search_products(self, text):

        self.search_text = text


        # جستجوی پیشرفته بعد از ساخت لیست کالا اضافه می‌شود
