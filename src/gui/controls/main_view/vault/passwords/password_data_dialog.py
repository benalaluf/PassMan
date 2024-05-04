import flet as ft

from src.data.db.password import PasswordData
from src.gui.controls.general.data_item import DataItemControl


class PasswordDataDialog(ft.UserControl):

    def __init__(self, password_data: PasswordData):
        super().__init__()
        self.password_data = password_data
        self.content = None
        self.init()

    def init(self):
        self.url_label = DataItemControl('URL/Name', self.password_data.url)
        self.url_label.data_lable.size = 30

        self.username_label = DataItemControl("Username", self.password_data.username)
        self.username_label.data_lable.size = 30

        self.password_label = DataItemControl("Password", self.password_data.password)
        self.password_label.data_lable.size = 30

        self.expr_date_label = DataItemControl("Date", self.password_data.date)
        self.expr_date_label.data_lable.size = 30

        self.img = ft.Icon(
            ft.icons.CREDIT_CARD,
            size=120,
            color=ft.colors.OUTLINE_VARIANT
        )

        self.card = ft.Container(
            content=(
                ft.Column(
                    controls=[

                        self.url_label,

                        self.username_label,
                        self.password_label,
                        self.expr_date_label

                    ],
                )
            ),
            width=600, height=300, alignment=ft.alignment.top_left
        )

        self.dialog = ft.AlertDialog(
            content=self.card,
            bgcolor=ft.colors.BACKGROUND,
        )

        self.content = self.dialog

    def open_dlg(self, e):
        e.control.page.dialog = self.dialog
        self.dialog.open = True
        e.control.page.update()

    def edit_password(self, password_data: PasswordData):
        self.url_label.set_data(password_data.url)
        self.username_label.set_data(password_data.username)
        self.password_label.set_data(password_data.password)
        self.expr_date_label.set_data(password_data.date)

    def build(self):
        return self.content
