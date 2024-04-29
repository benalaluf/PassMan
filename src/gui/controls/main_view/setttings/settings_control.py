import flet as ft
from flet_core import UserControl

from src.gui.Data import global_data


class SettingsControl(UserControl):

    def __init__(self):
        super().__init__()

    def build(self):

        content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            f"Settings",
                            size=50),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
        )
                ])
        return content


