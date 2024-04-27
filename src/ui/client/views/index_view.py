import flet as ft
from flet_core import UserControl

from src.ui.client.Data import State


class IndexView(UserControl):

    def __init__(self):
        super().__init__()

    def build(self):
        content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            "Welcome to PassMan",
                            size=50),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
        )
                ])
        return content


