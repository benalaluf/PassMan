import flet as ft
from flet_core import UserControl


class InDevelopmentControl(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        content = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Text("Feature in development :(", size=40),

                        border=ft.border.all(color=ft.colors.BLACK, width=2),
                        border_radius=14,
                        padding=40,
                        bgcolor=ft.colors.GREY_200
                    )

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center
        )
        return content
