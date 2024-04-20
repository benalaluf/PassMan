from typing import Union
import flet as ft
from flet_core import UserControl

from src.ui.client.Data import global_state
from src.ui.client.views.Router import Router


class DataView(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        text = ft.Text("State: " + global_state.get_state_by_key("data").get_state())
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
