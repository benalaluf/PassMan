from dataclasses import asdict

import flet as ft
from flet_core import UserControl, AppBar

from src.connections.client_conn import ClientConn


class MainBar(AppBar):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.menu_button = ft.IconButton(ft.icons.MENU, icon_color="white")
        self.init()


    def before_update(self):
        self.user_name_text.value = f"Wellcome, {ClientConn().user_data.username}"

    def init(self):
        self.title = ft.Row(
            [ft.Text("PassMan", color='white'), ft.Icon(name=ft.icons.LOCK_PERSON, color=ft.colors.WHITE)])
        self.bgcolor = ft.colors.RED
        # self.leading = self.menu_button
        self.user_name_text = ft.Text(f"Wellcome,", color="white")

        self.signout_button = ft.ElevatedButton(text="Signout", color="red", on_click=lambda _: self.page.go('/'))

        self.actions = [
            ft.Container(
                ft.Row(
                    [
                        self.user_name_text,
                        self.signout_button
                    ],
                    spacing=10)
                , padding=10)
        ]


    def signout(self, e):
        conn = ClientConn()
        conn.user_data = None
        print(asdict(conn.user_data))
        self.page.go('/')