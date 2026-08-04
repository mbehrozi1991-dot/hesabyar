from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty, NumericProperty


class SaleScreen(MDScreen):

    cart = ListProperty([])

    customer_name = StringProperty("")

    total_price = NumericProperty(0)


    def on_enter(self):
        self.reset_sale()


    def reset_sale(self):

        self.cart = []
        self.total_price = 0



    def add_to_cart(self, product, quantity):

        item = {
            "product": product,
            "quantity": quantity
        }

        self.cart.append(item)

        self.calculate_total()



    def calculate_total(self):

        total = 0

        for item in self.cart:

            total += item.get("price", 0) * item.get("quantity", 0)


        self.total_price = total



    def save_sale(self):

        app = self.manager.app

        if hasattr(app, "db"):

            # ثبت فاکتور در دیتابیس
            pass


        self.reset_sale()



    def remove_item(self, index):

        if index < len(self.cart):

            self.cart.pop(index)

            self.calculate_total()
