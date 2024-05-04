from flet_core import UserControl

from src.data.db.password import PasswordData
import flet as ft

from src.gui.controls.main_view.vault.passwords.password_data_dialog import PasswordDataDialog


class AddButton(UserControl):
    def __init__(self):
        super().__init__()
        self.content = None
        self.on_click = None
        self.init()

    def init(self):
        self.button = ft.Container(
            ft.Row(controls=[
                ft.Icon(
                    ft.icons.ADD,
                    color=ft.colors.WHITE
                ),
                ft.Text("Add", size=20, color=ft.colors.WHITE)
            ],
                alignment=ft.MainAxisAlignment.CENTER, spacing=3
            ),
            alignment=ft.alignment.center, bgcolor=ft.colors.RED, border_radius=10, ink=True, width=80, height=40,
            on_click= lambda _:self.on_click
        )
        self.content = self.button

    def build(self):
        return self.content
