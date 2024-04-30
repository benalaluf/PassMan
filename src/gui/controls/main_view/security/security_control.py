import flet as ft
from flet_core import UserControl

from src.gui.Data import global_data
from src.gui.controls.main_view.security.enable_2fa_control import EnableTwoFA
from src.gui.controls.main_view.security.security_container import SecurityContainer


class SecurityControl(UserControl):

    def __init__(self):
        super().__init__()
        self.two_fa_button = ft.ElevatedButton(text="Enable 2FA", width=200)
        self.two_fa_button.on_click = lambda _: self.page.go("/main/security/2fa")

        self.enable_two_fa = SecurityContainer(
                "Enable 2FA",
            "Enable 2FA to secure your account",
                    ft.Icon(ft.icons.VERIFIED_USER_ROUNDED, color=ft.colors.GREEN, size=50),
                    lambda _: self.page.go("/main/security/2fa")
        )

        self.options = ft.Container(
            ft.Column(
                controls=[
                    self.enable_two_fa
                ],
                expand=True,
                spacing=0,
            ),
            padding=ft.Padding(50, 0, 50, 0),
        )
        self.content = ft.Column(
            [
                ft.Text("Security", size=40, weight=ft.FontWeight.BOLD),
                self.options,

            ]
            , horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=50
        )
        self.enable_two_fa = EnableTwoFA()

    def build(self):


        return self.content


