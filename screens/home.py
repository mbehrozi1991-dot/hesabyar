from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout


class HomeScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        title = MDLabel(
            text="به حساب‌یار خوش آمدید",
            halign="center",
            font_style="H4"
        )

        layout.add_widget(title)

        self.add_widget(layout)
