import flet as ft
from flet_core import UserControl

from src.connections.client_conn import ClientConn


class LoginControl(UserControl):
    def __init__(self):
        super().__init__()
        self.title = ft.Text("Login", size=40, )
        self.username_field = ft.TextField(hint_text="Username", text_size=15, on_change=self.on_change)
        self.password_field = ft.TextField(hint_text="Password", password=True, can_reveal_password=True, text_size=15,
                                           on_change=self.on_change)

        self.login_button = ft.ElevatedButton(text="Login", width=200)
        self.login_button.on_click = self.login

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

    def login(self, e):
        conn = ClientConn()
        username = self.username_field.value
        password = self.password_field.value
        is_valid_input = self.validate_input()
        if is_valid_input:
            status = conn.login(username, password)
            if status == "Success":
                self.page.go('/main/vault/passwords')
            if status == "2fa":
                self.page.go('/auth/2fa')
            if status == "Fail":
                self.failed_login()

    def validate_input(self):
        valid = True
        if self.username_field.value == "":
            self.username_field.error_text = "Username is required"
            self.username_field.update()
            valid = False
        if self.password_field.value == "":
            self.password_field.error_text = "Password is required"
            self.password_field.update()
            valid = False

        return valid

    def failed_login(self):
        self.password_field.error_text = "Invalid username or password"
        self.password_field.update()

    def on_change(self, e):
        self.password_field.error_text = ""
        self.username_field.error_text = ""
        self.password_field.update()
        self.username_field.update()

    def before_update(self):
        self.username_field.value = ""
        self.password_field.value = ""
    def build(self):
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()
