from datetime import datetime

import flet as ft

from src.connections.client_conn import ClientConn
from src.data.db.password import PasswordData


class PasswordFormDialog(ft.UserControl):

    def __init__(self, password_data: PasswordData = None, add_password: callable = None,
                 edit_password: callable = None):

        super().__init__()
        self.password_data = password_data
        self.add_password = add_password
        self.edit_password = edit_password

        self.content = None
        self.url_field = ft.TextField(label="URL/Name", on_change=text_field_on_change)
        self.username_field = ft.TextField(label="Username", on_change=text_field_on_change)
        self.password_field = ft.TextField(label="Password", on_change=text_field_on_change)

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
        self.save_button.on_click = self.add_password_clicked

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
            bgcolor=ft.colors.BACKGROUND,
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

    def validate_input(self):
        valid = True
        if self.url_field.value == "":
            self.url_field.error_text = "URL/Name is required"
            self.url_field.update()
            valid = False
        if self.username_field.value == "":
            self.username_field.error_text = "Username is required"
            self.username_field.update()
            valid = False
        if self.password_field.value == "":
            self.password_field.error_text = "Password is required"
            self.password_field.update()
            valid = False
        return valid

    def add_password_clicked(self, e):
        is_valid = self.validate_input()
        if is_valid:
            if self.add_password:
                self.add_password(self.get_password_data())
            else:
                print(type(self.get_password_data()))
                self.edit_password(self.get_password_data())
            self.close_dlg()
            self.dialog.update()

    def close_dlg(self):
        self.dialog.open = False

    def get_password_data(self):
        password_data = PasswordData(
            self.url_field.value,
            self.username_field.value,
            self.password_field.value,
            self.get_current_date(),
        )
        if self.password_data:
            password_data.id = self.password_data.id

        return password_data

    def get_current_date(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d/%m/%y")
        return formatted_date

    def build(self):
        return self.content

def text_field_on_change(e):
    e.control.error_text = ""
    e.control.update()
