from flet_core import UserControl

from src.connections.client_conn import ClientConn
from src.data.items.password import PasswordData
import flet as ft

from src.gui.controls.main_view.vault.passwords.password_data_dialog import PasswordDataDialog
from src.gui.controls.main_view.vault.passwords.password_form_dialog import PasswordFormDialog


class PasswordContainer(UserControl):
    def __init__(self, password_data: PasswordData, remove_password, edit_password):
        super().__init__()
        self.password_data = password_data

        self.remove_password = remove_password
        self.edit_password = edit_password
        self.init()

    def init(self):
        self.copy_button = ft.IconButton(ft.icons.COPY, icon_color=ft.colors.BLUE,
                                         on_click=lambda e: self.page.set_clipboard(self.password_data.password))
        self.edit_button = ft.IconButton(ft.icons.EDIT, icon_color=ft.colors.BLUE)

        self.delete_button = ft.IconButton(ft.icons.DELETE, icon_color=ft.colors.RED)
        self.delete_button.on_click = self.remove_password_clicked

        self.edit_dialog = PasswordFormDialog(self.password_data, edit_password=self.save_edit_password)
        self.edit_button.on_click = self.edit_dialog.open_dlg

        self.view_dialog = PasswordDataDialog(self.password_data)

        self.url_label = ft.Text(self.password_data.url, size=20)
        self.username_label = ft.Text(self.password_data.username, size=15)

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
                                self.url_label,
                                self.username_label
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
            on_click=self.view_dialog.open_dlg,
            bgcolor=ft.colors.GREY_200, padding=ft.Padding(20, 0, 10, 0)

        )

    def save_edit_password(self, password_data: PasswordData):
        print("edited passwoerd niggerniggernib")
        self.password_data = password_data
        self.view_dialog.edit_password(password_data)
        self.edit_password_view()
        self.edit_password(password_data)
        self.update()
        self.edit_dialog.close_dlg()

    def edit_password_view(self):
        self.url_label.value = self.password_data.url
        self.username_label.value = self.password_data.username

    def remove_password_clicked(self, e):
        self.remove_password(self,self.password_data)

    def build(self):
        return self.content
