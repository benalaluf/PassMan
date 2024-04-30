import flet as ft
from flet_core import UserControl

from src.gui.Data import global_data
from src.gui.controls.main_view.security.enable_2fa_control import EnableTwoFA
from src.gui.controls.main_view.security.password_data_breach import PasswordDataBreach
from src.gui.controls.main_view.security.password_generator import PasswordGenerator
from src.gui.controls.main_view.security.security_container import SecurityContainer


class SecurityControl(UserControl):

    def __init__(self):
        super().__init__()

        self.data_breach_checker_control = PasswordDataBreach()
        self.enable_two_fa = EnableTwoFA()
        self.password_genarator = PasswordGenerator()

        self.enable_two_fa_option = SecurityContainer(
                "Enable 2FA",
            "Enable 2FA to secure your account",
                    ft.Icon(ft.icons.VERIFIED_USER_ROUNDED, color=ft.colors.GREEN, size=50),
                    lambda _: self.page.go("/main/security/2fa")
        )

        self.data_breach_checker_option = SecurityContainer(
            "Password Data-Breach Checker",
            "Check if your password has been compromised",
            ft.Icon(ft.icons.SECURITY, color=ft.colors.RED, size=50),
            lambda _: self.page.go("/main/security/password_breach")
        )

        self.password_genarator_option = SecurityContainer(
            "Password Generator",
            "Generate a strong password",
            ft.Icon(ft.icons.PASSWORD, color=ft.colors.BLUE, size=50),
            lambda _: self.page.go("/main/security/password_generator")
        )

        self.options = ft.Container(
            ft.Column(
                controls=[
                    self.enable_two_fa_option,
                    self.data_breach_checker_option,
                    self.password_genarator_option
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

    def build(self):
        return self.content


