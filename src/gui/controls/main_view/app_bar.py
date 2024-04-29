import flet as ft
from flet_core import UserControl, AppBar


class MainBar(AppBar):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.menu_button = ft.IconButton(ft.icons.MENU, icon_color="white")
        self.init()

    def init(self):
        self.title = ft.Row(
            [ft.Text("PassMan", color='white'), ft.Icon(name=ft.icons.LOCK_PERSON, color=ft.colors.WHITE)])
        self.bgcolor = ft.colors.RED
        # self.leading = self.menu_button
        self.user_name_text = ft.Text(f"Wellcome,", color="white")

        self.actions = [
            ft.Container(
                ft.Row(
                    [
                        self.user_name_text,
                        ft.ElevatedButton(text="Signout", color="red", on_click=lambda _: self.page.go('/'))
                    ],
                    spacing=10)
                , padding=10)
        ]


