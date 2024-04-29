from flet_core import UserControl, ListView
import flet as ft

from src.data.items.password import PasswordData
from src.gui.controls.main_view.vault.passwords.password_add_button import PasswordAddButton
from src.gui.controls.main_view.vault.passwords.password_container import PasswordContainer
from src.gui.controls.main_view.vault.passwords.password_form_dialog import PasswordFormDialog


class PasswordControl(UserControl):

    def __init__(self):
        super().__init__()
        self.content = None
        self.password_list = []
        self.init()

    def init(self):
        self.list = ft.ListView(
            controls=self.password_list,
            expand=True,
            width=900,
            spacing=10
        )

        self.add_button = PasswordAddButton()
        self.password_form = PasswordFormDialog()

        self.add_button.button.on_click = self.password_form.open_dlg

        self.password_counter = ft.Text("Passwords: " + str(len(self.password_list)), size=20)

        self.content = ft.Container(
            ft.Column(controls=[
                ft.Row(controls=[
                    self.password_counter,
                    self.add_button,
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=900),
                self.list
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            , padding=ft.Padding(10, 10, 10, 10))

    def append_password(self, password):
        self.password_list.append(PasswordContainer(PasswordData(**password)))
        self.password_counter.value = f"Passwords: {len(self.password_list)} "

    def update_passwords(self, passwords):
        # self.password_list = []
        for password in passwords:
            self.password_list.append(PasswordContainer(PasswordData(**password)))
        self.password_counter.value = f"Passwords: {len(self.password_list)} "

    def build(self):
        return self.content
