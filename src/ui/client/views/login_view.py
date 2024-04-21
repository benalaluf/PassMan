import flet as ft
from flet_core import UserControl


class LoginView(UserControl):
    def __init__(self):
        super().__init__()
        self.title = ft.Text("Login", size=40, )
        self.username_filed = ft.TextField(hint_text="Username", text_size=15)
        self.password_field = ft.TextField(hint_text="Password", text_size=15)
        self.login_button = ft.ElevatedButton(text="Login", on_click=self.login, width=200)

        self.content = ft.AlertDialog(content=ft.Column(
            [
                self.title,
                self.username_filed,
                self.password_field,
                self.login_button
            ]
            , width=400, height=400, horizontal_alignment=ft.CrossAxisAlignment.CENTER))

        self.login_button.on_click = self.login

        self.content.on_dismiss = lambda e: self.page.go("/")

    def build(self):
        self.content.open = True
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()

    def login(self, e):
        print(self.username_filed.value, self.password_field.value)
