from flet_core import UserControl

from src.connections.client_conn import ClientConn
from src.data.items.password import PasswordData
import flet as ft

from src.gui.controls.main_view.vault.passwords.password_data_dialog import PasswordDataDialog
from src.gui.controls.main_view.vault.passwords.password_form_dialog import PasswordFormDialog


class PasswordContainer(UserControl):
    def __init__(self, password_data: PasswordData, remove_password):
        super().__init__()
        self.password_data = password_data
        self.remove_password = remove_password
        self.edit_dialog = PasswordFormDialog(self.password_data)
        self.init()

    def init(self):

        self.copy_button = ft.IconButton(ft.icons.COPY, icon_color=ft.colors.BLUE,
                                         on_click=lambda e: self.page.set_clipboard(self.password_data.password))
        self.edit_button = ft.IconButton(ft.icons.EDIT, icon_color=ft.colors.BLUE)

        self.edit_button.on_click = self.edit_dialog.open_dlg

        self.delete_button = ft.IconButton(ft.icons.DELETE, icon_color=ft.colors.RED)
        self.delete_button.on_click = self.remove_password_clicked
        self.dialog = PasswordDataDialog(self.password_data)
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
                        ft.Row(controls=[
                            self.delete_button,
                            self.edit_button,
                            self.copy_button,

                        ],
                            spacing=3,
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
            ,

            alignment=ft.alignment.center,
            height=80,
            border_radius=10,
            ink=True,
            on_click=self.dialog.open_dlg,
            bgcolor=ft.colors.GREY_200, padding=ft.Padding(20, 0, 10, 0)

        )


    def remove_password_clicked(self,e):
        self.remove_password(self)

    def build(self):
        return self.content
