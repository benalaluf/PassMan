import flet as ft
from flet_core import UserControl



class DataView(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        text = ft.Text("State: " )
        self.content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            "Data View",
                            size=50),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        text,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
        return self.content
