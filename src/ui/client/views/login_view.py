import flet as ft
from flet_core import UserControl


class LoginView(UserControl):
    def __init__(self):
        super().__init__()

        self.title = ft.Text("Login", size=40, )
        self.username_filed = ft.TextField(hint_text="Username", text_size=15)
        self.password_field = ft.TextField(hint_text="Password", text_size=15)
        self.login_button = ft.ElevatedButton(text="Login", width=200)

        self.content = ft.Container(
            content=ft.Column(
                [
                    self.title,
                    self.username_filed,
                    self.password_field,
                    self.login_button
                ],
                 horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE,
            border_radius=10,
            width=400, height=400
        )

    def build(self):

        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()
