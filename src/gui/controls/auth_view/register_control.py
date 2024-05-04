import flet as ft
from flet_core import UserControl

from src.connections.client_conn import ClientConn
from src.misc.input_validation import validate_mail


class RegisterControl(UserControl):

    def __init__(self):
        super().__init__()
        self.title = ft.Text("Register", size=40, )
        self.mail_field = ft.TextField(hint_text="Mail", text_size=15, on_change=self.on_change)
        self.username_field = ft.TextField(hint_text="Username", text_size=15, on_change=self.on_change)
        self.password_field = ft.TextField(hint_text="Password", text_size=15, password=True, can_reveal_password=True,
                                           on_change=self.on_change)
        self.register_button = ft.ElevatedButton(text="Register", width=200)
        self.register_button.on_click = self.register

        self.register = ft.Container(ft.Column(
            [
                self.title,
                self.mail_field,
                self.username_field,
                self.password_field,
                self.register_button
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
            self.register,
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.GREY_700
        )

    def register(self, e):
        conn = ClientConn()
        mail = self.mail_field.value
        username = self.username_field.value
        password = self.password_field.value
        is_valid_input = self.validate_input()
        if is_valid_input:
            status = conn.register(username, password, mail)
            if status:
                self.page.go('/main/vault/passwords')
            else:
                self.failed_register()

    def validate_input(self):
        valid = True
        if not validate_mail(self.mail_field.value):
            self.mail_field.error_text = "Invalid mail"
            self.mail_field.update()
            valid = False
        if self.username_field.value == "":
            self.username_field.error_text = "Username is required"
            self.username_field.update()
            valid = False
        if self.password_field.value == "":
            self.password_field.error_text = "Password is required"
            self.password_field.update()
            valid = False
        if self.mail_field.value == "":
            self.mail_field.error_text = "Mail is required"
            self.mail_field.update()
            valid = False

        return valid

    def failed_register(self):
        self.username_field.error_text = "username allready exists"
        self.username_field.update()

    def invalid_register(self):
        self.password_field.error_text = "Invalid username or password or mail"
        self.password_field.update()

    def on_change(self, e):
        self.username_field.error_text = ""
        self.password_field.error_text = ""
        self.mail_field.error_text = ""
        self.username_field.update()
        self.password_field.update()
        self.mail_field.update()
    def before_update(self):
        self.mail_field.value = ""
        self.username_field.value = ""
        self.password_field.value = ""
    def build(self):
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()


