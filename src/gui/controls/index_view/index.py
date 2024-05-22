import flet as ft
from flet_core import UserControl


class IndexControl(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        content = ft.Column(
            [
                ft.Text(
                    f"Welcome to PassMan",
                    size=50),

                ft.Container(height=100),
                ft.Container(
                    ft.Column(
                        controls=[
                            ft.Text("Your Secure Password Management Solution", size=40),

                            ft.Text("Why Choose PassMan?", size=30),
                            ft.Text(
                                """In today’s digital age, security is paramount. 
    PassMan is designed to keep your online accounts safe and secure, offering an easy-to-use interface with
    robust security features. Whether you're managing passwords for personal use or for an entire organization,
    PassMan has you covered.
                                """, size=20
                            ),
                        ], horizontal_alignment=ft.CrossAxisAlignment.START
                    ),
                    border=ft.border.all(color=ft.colors.BLACK, width=2),
                    border_radius=14,
                    padding=40,
                    bgcolor=ft.colors.GREY_200
                )

            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        return content
