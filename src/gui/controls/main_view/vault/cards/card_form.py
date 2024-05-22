import flet as ft

from src.data.db.card import CardData
from src.data.db.password import PasswordData
from src.gui.controls.general.data_item import DataItemControl
from src.gui.controls.general.date_drop_down import DateDropDown


class CardForm(ft.UserControl):

    def __init__(self, add_card=None):
        super().__init__()
        self.add_card = add_card
        self.content = None
        self.init()

    def init(self):
        number_input_filter = ft.InputFilter(r'[0-9]')

        self.save_button = ft.TextButton("save", on_click=self.add_card_clicked)

        self.bank_name_label = ft.TextField(label="Bank Name", on_change=text_field_on_change)
        self.bank_name_label.text_size = 40

        self.card_number_label = ft.TextField(label="Card Number", on_change=text_field_on_change)
        self.card_number_label.text_size = 40
        self.card_number_label.input_filter = number_input_filter

        self.card_cvv_label = ft.TextField(label="CVV Number", on_change=text_field_on_change)
        self.card_cvv_label.text_size = 26
        self.card_cvv_label.input_filter = number_input_filter

        self.expr_date_label = DateDropDown(20,30)

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
                                ft.Container(
                                    self.expr_date_label, alignment=ft.alignment.center
                                )

                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN

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
        self.bank_name_label.value = ''
        self.card_number_label.value = ''
        self.card_cvv_label.value = ''
        self.expr_date_label.clear_data()


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
            self.expr_date_label.get_data()
        )

        return card_data

    def validate_input(self):
        valid = True
        if self.bank_name_label.value == "":
            self.bank_name_label.error_text = "Bank Name is required"
            self.bank_name_label.update()
            valid = False
        if self.card_number_label.value == "":
            self.card_number_label.error_text = "Card Number is required"
            self.card_number_label.update()
            valid = False
        if self.card_cvv_label.value == "":
            self.card_cvv_label.error_text = "CVV Number is required"
            self.card_cvv_label.update()
            valid = False
        if self.expr_date_label.get_data() == "":
            self.expr_date_label.error_text = "Date is required"
            self.expr_date_label.update()
            valid = False
        return valid

    def add_card_clicked(self, e):
        is_valid = self.validate_input()
        if is_valid:
            self.add_card(self.get_card_data())
            self.dialog.open = False
            self.dialog.update()

    def build(self):
        return self.content


def text_field_on_change(e):
    e.control.error_text = ""
    e.control.update()
