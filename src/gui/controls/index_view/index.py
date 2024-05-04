import flet as ft
from flet_core import UserControl



class IndexControl(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            f"Welcome to PassMan",
                            size=50),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
        )
                ])
        return content


