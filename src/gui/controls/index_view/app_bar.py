import flet as ft
from flet_core import UserControl, AppBar


class IndexBar(AppBar):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.init()

    def init(self):
        self.title = ft.Row(
            [ft.Text("PassMan", color='white'), ft.Icon(name=ft.icons.LOCK_PERSON, color=ft.colors.WHITE)])
        self.center_title = False
        self.bgcolor = ft.colors.RED

        self.actions = [
            ft.Container(
                ft.Row(
                    [
                        ft.ElevatedButton(text="Login", color="red", on_click=lambda _: self.page.go('/login')),
                        ft.ElevatedButton(text="Register", color="red", on_click=lambda _: self.page.go('/register'))
                    ],
                    spacing=5)
                , padding=10)
        ]
