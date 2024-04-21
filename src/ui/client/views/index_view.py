import flet as ft
from flet_core import UserControl

from src.ui.client.Data import State


class IndexView(UserControl):

    def __init__(self):
        super().__init__()

    def build(self):
        self.text_field = ft.TextField()
        self.send_button = ft.ElevatedButton("Send")
        self.send_button.on_click = self.send_data
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

    def send_data(self, e: ft.ControlEvent):
        State("data", self.text_field.value)
        e.page.go("/data")
