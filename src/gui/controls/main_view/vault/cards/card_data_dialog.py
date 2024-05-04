import flet as ft

from src.data.db.card import CardData
from src.data.db.password import PasswordData
from src.gui.controls.general.data_item import DataItemControl


class CardDialog(ft.UserControl):

    def __init__(self, card_data: CardData, edit_card=None):
        super().__init__()
        self.card_data = card_data
        self.edit_card = edit_card
        self.content = None
        self.init()

    def init(self):

        self.save_button = ft.TextButton("save", on_click=self.save_card)
        self.save_button.visible = False

        self.edit_button = ft.IconButton(ft.icons.EDIT, on_click=self.edit_card_clicked)

        self.bank_name_label = DataItemControl('Bank Name', self.card_data.bank_name)
        self.bank_name_label.data_lable.size = 40
        self.bank_name_label.data_field.text_size = 40

        card_nuber_str = ''.join(
            self.card_data.card_number[i:i + 4] for i in range(0, len(self.card_data.card_number), 4))

        self.card_number_label = DataItemControl("Card Number", card_nuber_str)
        self.card_number_label.data_lable.size = 40
        self.card_number_label.data_field.text_size = 40

        self.card_cvv_label = DataItemControl("CVV Number", self.card_data.cvv)
        self.card_cvv_label.data_lable.size = 26
        self.card_cvv_label.data_field.text_size = 26

        self.expr_date_label = DataItemControl("Expiration Date", self.card_data.expr_date)
        self.expr_date_label.data_lable.size = 26
        self.expr_date_label.data_field.text_size = 26

        self.img = ft.Icon(
            ft.icons.CREDIT_CARD,
            size=120,
            color=ft.colors.OUTLINE_VARIANT
        )

        self.card = ft.Container(
            content=(
                ft.Column(
                    controls=[

                        ft.Row(
                            controls=[
                                ft.Text("CARD INFO", size=20, weight=ft.FontWeight.W_500),
                                self.edit_button,
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
            self.bank_name_label.get_data(),
            self.card_number_label.get_data(),
            self.card_cvv_label.get_data(),
            self.expr_date_label.get_data()
        )

        card_data.id = self.card_data.id
        return card_data


    def set_card_data(self, card_data: CardData):
        self.bank_name_label.set_data(card_data.bank_name)
        self.card_number_label.set_data(card_data.card_number)
        self.card_cvv_label.set_data(card_data.cvv)
        self.expr_date_label.set_data(card_data.expr_date)
    def edit_card_clicked(self, e):
        self.save_button.visible = True
        self.save_button.update()
        self.edit_button.visible = False
        self.edit_button.update()
        self.bank_name_label.edit()
        self.card_number_label.edit()
        self.card_cvv_label.edit()
        self.expr_date_label.edit()

    def save_card(self, e):
        self.save_button.visible = False
        self.save_button.update()
        self.edit_button.visible = True
        self.edit_button.update()
        self.bank_name_label.view()
        self.card_number_label.view()
        self.card_cvv_label.view()
        self.expr_date_label.view()
        self.edit_card(self.get_card_data())
        self.set_card_data(self.get_card_data())




    def build(self):
        return self.content

