import flet as ft
from flet_core import UserControl


class LoginView(UserControl):

    def __init__(self):
        super().__init__()

    def build(self):
        self.content = ft.Column(
            [

                ft.Text("Login", size=30),
                ft.TextField(hint_text="Username"),
                ft.TextField(hint_text="Password"),
                ft.ElevatedButton(text="Login", on_click=self.login)
            ]

        )
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()

    def login(self, e):
        pass
