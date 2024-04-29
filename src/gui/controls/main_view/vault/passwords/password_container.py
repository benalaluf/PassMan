from flet_core import UserControl

from src.data.items.password import PasswordData
import flet as ft

class PasswordContainer(UserControl):
    def __init__(self, password_data: PasswordData):
        super().__init__()
        self.password_data = password_data
        self.init()

    def init(self):
        self.copy_button = ft.IconButton(ft.icons.COPY, icon_color=ft.colors.BLUE,
                                         on_click=lambda e: print("Copy clicked!"))
        self.content = ft.Container(
            content=ft.Row(
                [
                    ft.Row([
                        ft.Container(
                            ft.Icon(
                                ft.icons.LOCK,
                                color=ft.colors.BLUE
                            ),
                            padding=ft.Padding(0, 0, 10, 0)
                        ),
                        ft.Container(
                            ft.Column([
                                ft.Text(self.password_data.url, size=20),
                                ft.Text(self.password_data.username, size=15)
                            ],
                                spacing=5,
                                alignment=ft.MainAxisAlignment.CENTER)
                        )
                    ]),
                    ft.Container(
                        self.copy_button
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            alignment=ft.alignment.center,
            height=80,
            border_radius=10,
            ink=True,
            on_click=lambda e: print("Clickable transparent with Ink clicked!"),
            bgcolor=ft.colors.GREY_200, padding=ft.Padding(20, 0, 10, 0))

    def build(self):
        return self.content