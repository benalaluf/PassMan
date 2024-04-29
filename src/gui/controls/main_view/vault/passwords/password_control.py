from flet_core import UserControl, ListView
import flet as ft

from src.data.items.password import PasswordData
from src.gui.controls.main_view.vault.passwords.password_container import PasswordContainer


class PasswordControl(UserControl):

    def __init__(self):
        super().__init__()
        self.content = None
        self.init()

    def init(self):
        self.password_list = [
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),
            PasswordContainer(PasswordData("https://www.google.com", "test", "test", "test")),

        ]
        self.list = ft.ListView(
            controls=self.password_list,
            expand=True,
            width=900,
            spacing=10
        )

        self.content = ft.Container(self.list, padding=ft.Padding(10, 10, 10, 10))

    def update_passwords(self, passwords):
        self.password_list = passwords
        self.list.update()

    def append_password(self, password):
        self.password_list.append(password)
        self.list.update()

    def build(self):
        return self.content
