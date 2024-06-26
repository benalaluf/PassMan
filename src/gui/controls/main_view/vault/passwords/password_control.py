from flet_core import UserControl
import flet as ft

from src.connections.client_conn import ClientConn
from src.data.db.password import PasswordData
from src.gui.controls.general.add_button import AddButton
from src.gui.controls.main_view.vault.passwords.password_container import PasswordContainer
from src.gui.controls.main_view.vault.passwords.password_form_dialog import PasswordFormDialog


class PasswordControl(UserControl):

    def __init__(self):
        super().__init__()
        self.content = None
        self.init()

    def init(self):
        self.passwords = ft.Column(
            expand=True,
            width=900,
            spacing=10
        )

        self.passwords.scroll = ft.ScrollMode.ALWAYS

        self.add_button = AddButton()
        self.password_form = PasswordFormDialog(add_password=self.add_password)

        self.add_button.button.on_click = self.password_form.open_dlg

        self.password_counter = ft.Text("Passwords: " + str(len(self.passwords.controls)), size=20)

        self.view = ft.Container(
            ft.Column(controls=[
                ft.Row(controls=[
                    self.password_counter,
                    self.add_button,
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=900),
                self.passwords
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            , padding=ft.Padding(10, 10, 10, 10))
    def append_password(self, password: PasswordData):
        password_container = PasswordContainer(password, self.remove_password, self.edit_password)
        self.passwords.controls.append(password_container)
        self.password_counter.value ="Passwords: " + str(len(self.passwords.controls))
    def add_password(self, password: PasswordData):
        ClientConn().add_password(password)
        self.update()

    def remove_password(self, password_data):
        ClientConn().delete_pass(password_data)
        self.update()

    def edit_password(self, password:PasswordData):
        ClientConn().add_password(password)
        self.update()

    def before_update(self):
        conn = ClientConn()
        items = conn.get_user_items()
        self.passwords.controls.clear()
        if items:

            print(items)
            passwords = items.get('password')
            cards = items.get('card')
            if passwords:
                for password in passwords:
                    self.append_password(PasswordData(**password))


            if cards:
                pass

            self.password_counter.value ="Passwords: " + str(len(self.passwords.controls))
        else:
            print("faild to get items")


    def build(self):
        return self.view
