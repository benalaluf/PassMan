import flet as ft
from flet_core import UserControl


class LoginControl(UserControl):
    def __init__(self):
        super().__init__()
        self.title = ft.Text("Login", size=40, )
        self.username_field = ft.TextField(hint_text="Username", text_size=15)
        self.password_field = ft.TextField(hint_text="Password",  password=True, can_reveal_password=True,text_size=15)
        self.login_button = ft.ElevatedButton(text="Login", width=200)

        self.login = ft.Container(ft.Column(
            [
                self.title,
                self.username_field,
                self.password_field,
                self.login_button
            ],
            width=400,
            height=400,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            border_radius=14,
            bgcolor=ft.colors.WHITE,
            padding=20,
            border=ft.border.all(color=ft.colors.BLACK, width=2),
        )

        self.content = ft.Container(
            self.login,
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.GREY_700
            )


    def build(self):
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()
