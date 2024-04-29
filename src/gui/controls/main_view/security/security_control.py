import flet as ft
from flet_core import UserControl

from src.gui.Data import global_data


class SecurityControl(UserControl):

    def __init__(self):
        super().__init__()

    def build(self):

        content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            f"Security",
                            size=50),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
        )
                ])
        return content

