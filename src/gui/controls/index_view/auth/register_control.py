import flet as ft
from flet_core import UserControl


class RegisterControl(UserControl):

    def __init__(self):
        super().__init__()
        self.title = ft.Text("Register", size=40, )
        self.mail_field = ft.TextField(hint_text="Mail", text_size=15, on_change=self.on_change)
        self.username_field = ft.TextField(hint_text="Username", text_size=15, on_change=self.on_change)
        self.password_field = ft.TextField(hint_text="Password", text_size=15, password=True, can_reveal_password=True, on_change=self.on_change)
        self.login_button = ft.ElevatedButton(text="Register", width=200)


        self.register = ft.Container(ft.Column(
            [
                self.title,
                self.mail_field,
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
            self.register,
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.GREY_700
        )

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


    def build(self):
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()

    def register(self, e):
        print(self.username_field.value, self.password_field.value)
