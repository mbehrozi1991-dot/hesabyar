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

        app = self.manager.app

        if hasattr(app, "db"):

            c = app.db.conn.cursor()

            c.execute("DELETE FROM customers WHERE id=?", (customer_id,))

            app.db.conn.commit()

        self.load_customers()


    def edit_customer(self, customer_id, name, phone, address=""):

        app = self.manager.app

        if hasattr(app, "db"):

            c = app.db.conn.cursor()

            c.execute("""
            UPDATE customers
            SET name=?, phone=?, address=?
            WHERE id=?
            """, (name, phone, address, customer_id))

            app.db.conn.commit()

        self.load_customers()


    def search_customers(self, text):

        self.search_text = text

        if text == "":
            self.load_customers()
            return

        app = self.manager.app
        filtered_customers = []

        if hasattr(app, "db"):

            c = app.db.conn.cursor()

            c.execute("""
            SELECT * FROM customers
            WHERE store_id=1 AND name LIKE ?
            """, (f"%{text}%",))

            for item in c.fetchall():
                filtered_customers.append(item)

        self.customers = filtered_customers
