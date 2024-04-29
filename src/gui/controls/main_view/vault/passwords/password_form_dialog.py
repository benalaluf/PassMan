from datetime import datetime

import flet as ft

from src.data.items.password import PasswordData


class PasswordFormDialog(ft.UserControl):

    def __init__(self, password_data: PasswordData = None):
        super().__init__()
        self.password_data = password_data
        self.content = None
        self.url_field = ft.TextField(label="URL/Name")
        self.username_field = ft.TextField(label="Username")
        self.password_field = ft.TextField(label="Password")

        if password_data:
            self.text = "Password Edit"
            self.url_field.value = password_data.url
            self.username_field.value = password_data.username
            self.password_field.value = password_data.password
        else:
            self.text = "Add Password"
        self.init()

    def init(self):
        self.title = ft.Row(controls=[
            ft.Icon(ft.icons.LOCK, size=30, color=ft.colors.BLUE),
            ft.Text(self.text, size=30, color=ft.colors.BLUE)
        ])

        self.save_button = ft.TextButton("Save")

        self.password_data_container = ft.Container(
            ft.Column(controls=[
                self.url_field,
                self.username_field,
                self.password_field,
            ]
            ),
            width=700, height=300,

        )

        self.dialog = ft.AlertDialog(
            title=self.title,
            content=self.password_data_container,
            bgcolor=ft.colors.WHITE,
            actions=[self.save_button]
        )

        self.content = self.dialog

    def open_dlg(self, e):
        if not self.password_data:
            self.url_field.value = ""
            self.username_field.value = ""
            self.password_field.value = ""
        e.control.page.dialog = self.dialog
        self.dialog.open = True
        e.control.page.update()

    def save_edit(self):
        pass

    def close_dlg(self, e):
        self.dialog.open = False
        e.control.page.update()

    def get_password_data(self):
        password_data = PasswordData(
            self.url_field.value,
            self.username_field.value,
            self.password_field.value,
            self.get_current_date()
        )

        return password_data

    def get_current_date(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d/%m/%y")
        return formatted_date

    def build(self):
        return self.content
