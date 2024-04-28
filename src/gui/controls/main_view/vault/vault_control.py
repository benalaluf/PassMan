import flet as ft
from flet_core import UserControl

from src.gui.controls.main_view.vault.password_control import PasswordControl
from src.gui.controls.main_view.vault.vault_nav import VaultNavigationRail



class VaultControl(UserControl):
    def __init__(self):
        super().__init__()
        self.body = ft.Container(alignment=ft.alignment.center, expand=True, padding=0)
        self.content = ft.Row(
            [
                VaultNavigationRail(self.page),
                self.body

            ]
        )
        self.passwords_control = PasswordControl()
        self.passwords_control.add_passwords(["password1", "password2", "password3"])

    def build(self):
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()
