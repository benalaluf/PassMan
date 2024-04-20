import flet as ft
from flet_core import UserControl


class RegisterView(UserControl):

    def __init__(self):
        super().__init__()

    def build(self):
        self.content = ft.Column(

            [
                ft.Row(
                    [
                        ft.Text("My Profile", size=30),
                        ft.IconButton(icon=ft.icons.PERSON_ROUNDED, icon_size=30),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Image(src=f"/banner.png", width=200, border_radius=100)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Text("Name: CodingJQ")
                    ],
                ),
                ft.Row(
                    [
                        ft.Text("Member Since: 2023")
                    ]
                ),
                ft.Row(
                    [
                        ft.Text("Github: https://github.com/CodingJQ")
                    ]
                )

            ]
        )
        return self.content
