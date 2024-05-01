import flet as ft

from src.data.items.card import CardData
from src.data.items.password import PasswordData
from src.gui.controls.general.data_item import DataItemControl


class CardForm(ft.UserControl):

    def __init__(self, add_card=None):
        super().__init__()
        self.add_card = add_card
        self.content = None
        self.init()

    def init(self):
        self.save_button = ft.TextButton("save", on_click=self.add_card_clicked)

        self.bank_name_label = ft.TextField(label="Bank Name")
        self.bank_name_label.text_size = 40

        self.card_number_label = ft.TextField(label="Card Number")
        self.card_number_label.text_size = 40

        self.card_cvv_label = ft.TextField(label="CVV Number")
        self.card_cvv_label.text_size = 26

        self.expr_date_label = ft.TextField("Expiration Date")
        self.expr_date_label.text_size = 26

        self.card = ft.Container(
            content=(
                ft.Column(
                    controls=[

                        ft.Row(
                            controls=[
                                ft.Text("CARD INFO", size=20, weight=ft.FontWeight.W_500),
                                self.save_button,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        self.bank_name_label,

                        self.card_number_label,

                        ft.Row(
                            controls=[
                                self.card_cvv_label,
                                self.expr_date_label

                            ],

                            spacing=20
                        ),
                    ],
                )
            ),
            width=600, height=400, alignment=ft.alignment.top_left
        )

        self.dialog = ft.AlertDialog(
            content=self.card,
            bgcolor=ft.colors.BACKGROUND,
        )

        self.content = self.dialog

    def open_dlg(self, e):
        print("open dialog")
        e.control.page.dialog = self.dialog
        self.dialog.open = True
        e.control.page.update()

    def close_dlg(self):
        self.dialog.open = False

    def get_card_data(self):
        card_data = CardData(
            self.bank_name_label.value,
            self.card_number_label.value,
            self.card_cvv_label.value,
            self.expr_date_label.value
        )

        return card_data

    def add_card_clicked(self, e):
        self.add_card(self.get_card_data())
        self.dialog.open = False
        self.dialog.update()

    def build(self):
        return self.content
