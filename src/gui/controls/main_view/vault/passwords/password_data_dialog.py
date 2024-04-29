import flet as ft

from src.data.items.password import PasswordData


class PasswordDataDialog(ft.UserControl):

    def __init__(self, password_data: PasswordData):
        super().__init__()
        self.password_data = password_data
        self.content = None
        self.init()

    def init(self):
        self.password_data_container = ft.Container(
            ft.Column(controls=[
                ft.Icon(ft.icons.LOCK, size=30, color=ft.colors.BLUE),
                ft.Text("URL: " + self.password_data.url, size=20),
                ft.Text("Username: " + self.password_data.username, size=20),
                ft.TextField("Password: " + self.password_data.password,
                             text_size=20,
                             can_reveal_password=True,
                             password=True,
                             border=ft.InputBorder.NONE),
                ft.Text("date: " + self.password_data.date, size=20),
            ]
            ),
            width=400, height=200,
        )

        self.dialog = ft.AlertDialog(
            content=self.password_data_container,
            bgcolor=ft.colors.WHITE
        )

        self.content = self.dialog

    def open_dlg(self, e):
        e.control.page.dialog = self.dialog
        self.dialog.open = True
        e.control.page.update()

    def build(self):
        return self.content
