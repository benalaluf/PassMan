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
                ft.Text("URL: " + self.password_data.url, size=16),
                ft.Text("Username: " + self.password_data.username, size=16),
                ft.Text("Password: " + self.password_data.password, size=16),
                ft.Text("date: " + self.password_data.date, size=16)
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
