import flet as ft
from flet_core import UserControl


class RegisterView(UserControl):

    def __init__(self):
        super().__init__()
        self.title = ft.Text("Register", size=40, )
        self.mail_field = ft.TextField(hint_text="Mail", text_size=15)
        self.username_field = ft.TextField(hint_text="Username", text_size=15)
        self.password_field = ft.TextField(hint_text="Password", text_size=15)
        self.login_button = ft.ElevatedButton(text="Register", width=200)

        self.content = ft.AlertDialog(content=ft.Column(
            [
                self.title,
                self.mail_field,
                self.username_field,
                self.password_field,
                self.login_button
            ]
            , width=400, height=600, horizontal_alignment=ft.CrossAxisAlignment.CENTER))


        self.content.on_dismiss = lambda e: self.page.go("/")

    def build(self):
        self.content.open = True
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()

    def register(self, e):
        print(self.username_field.value, self.password_field.value)
