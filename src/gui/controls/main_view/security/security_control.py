import flet as ft
from flet_core import UserControl

from src.gui.Data import global_data
from src.gui.controls.main_view.security.enable_2fa_control import EnableTwoFA


class SecurityControl(UserControl):

    def __init__(self):
        super().__init__()
        self.body = ft.Container(alignment=ft.alignment.center, expand=True, padding=0)
        self.two_fa_button = ft.ElevatedButton(text="Enable 2FA", width=200)
        self.two_fa_button.on_click = lambda _: self.page.go("/main/security/2fa")
        self.content = ft.Row(
            [
                ft.Text("Security"),
                self.two_fa_button,
                self.body

            ]
        )
        self.enable_two_fa = EnableTwoFA()

    def build(self):


        return self.content


