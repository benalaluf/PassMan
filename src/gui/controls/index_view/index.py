import flet as ft
from flet_core import UserControl

from src.gui.Data import global_data


class IndexControl(UserControl):

    def __init__(self):
        super().__init__()

    def build(self):
        username = global_data.get_state_by_key("username")
        if username is None:
            username = ""
        else:
            username = f", {username.get_state()}"
        content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            f"Welcome to PassMan{username}",
                            size=50),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
        )
                ])
        return content


