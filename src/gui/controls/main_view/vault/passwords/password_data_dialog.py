import flet as ft

from src.data.items.password import PasswordData


class PasswordDataDialog(ft.UserControl):

    def __init__(self, password_data: PasswordData):
        super().__init__()
        self.password_data = password_data
        self.content = None
        self.init()

    def init(self):
        self.url_label = ft.Text("URL/Name" + self.password_data.url, size=20)
        self.username_label = ft.Text("Username: " + self.password_data.username, size=20)
        self.password_label = ft.TextField("Password: " + self.password_data.password,
                                           text_size=20,
                                           can_reveal_password=True,
                                           password=True,
                                           border=ft.InputBorder.NONE)
        self.date_label = ft.Text("Date:" + self.password_data.date, size=20)

        self.password_data_container = ft.Container(
            ft.Column(controls=[
                self.url_label,
                self.username_label,
                self.password_label,
                self.date_label,

            ]
            ),
            width=400, height=200,
        )

        self.dialog = ft.AlertDialog(
            content=self.password_data_container,
            bgcolor=ft.colors.BACKGROUND,
        )

        self.content = self.dialog

    def open_dlg(self, e):
        e.control.page.dialog = self.dialog
        self.dialog.open = True
        e.control.page.update()

    def edit_password(self, password_data: PasswordData):
        self.url_label.value = password_data.url
        self.username_label.value = password_data.username
        self.password_label.value = password_data.password
        self.date_label.value = password_data.date

    def build(self):
        return self.content
