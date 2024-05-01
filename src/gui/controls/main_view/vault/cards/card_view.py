from flet_core import UserControl

from src.connections.client_conn import ClientConn
from src.data.items.card import CardData
from src.data.items.password import PasswordData
import flet as ft

from src.gui.controls.main_view.vault.cards.card_data_dialog import CardDialog
from src.gui.controls.main_view.vault.passwords.password_data_dialog import PasswordDataDialog
from src.gui.controls.main_view.vault.passwords.password_form_dialog import PasswordFormDialog


class CardView(UserControl):
    def __init__(self, card_data: CardData):
        super().__init__()
        self.card_data = card_data

        self.init()

    def init(self):
        self.card_dialog = CardDialog(self.card_data)


        self.delete_button = ft.IconButton(ft.icons.DELETE, icon_color=ft.colors.RED)
        self.delete_button.visible =False


        self.bank_name_label = ft.Text(
            self.card_data.bank_name,
            size=25,
            weight=ft.FontWeight.BOLD
        )

        self.card_number_label = ft.Text(
            "**** **** **** " + self.card_data.card_number[-4:],
            size=20,
            weight=ft.FontWeight.BOLD
        )

        self.card_cvv_label = ft.Text(
            "**" + self.card_data.cvv[-1],
            size=13,
            weight=ft.FontWeight.BOLD
        )
        self.img = ft.Icon(
            ft.icons.CREDIT_CARD,
            size=60,
            color=ft.colors.OUTLINE_VARIANT
        )

        self.card = ft.Container(
            content=(
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Column(
                                    spacing=1,
                                    controls=[
                                        ft.Text(
                                            'BANK NAME',
                                            size=10,
                                            weight=ft.FontWeight.W_500,
                                        ),
                                        self.bank_name_label
                                    ],
                                ),
                                self.delete_button
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),


                        ft.Container(
                            padding=ft.padding.only(top=10, bottom=18),
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Column(
                                    spacing=1,
                                    controls=[

                                        ft.Text(
                                            'CARD NUMBER',
                                            size=10,
                                            weight=ft.FontWeight.W_500,
                                        ),
                                        self.card_number_label,

                                        ft.Container(
                                            alignment=ft.alignment.bottom_left,
                                            content=ft.Text(
                                                'CVV NUMBER',
                                                size=9,
                                                weight=ft.FontWeight.W_500,
                                            ),
                                        ),
                                        self.card_cvv_label
                                    ],
                                ),
                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.END,
                                    controls=[self.img],
                                ),
                            ],
                        ),
                    ],
                )
            ),
            padding=ft.padding.all(12),
            margin=ft.margin.all(-5),
            width=310,
            height=185,
            border_radius=ft.border_radius.all(18),
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            ink=True,
            on_click= self.card_dialog.open_dlg,
            on_hover=self.show_delete_button,

        )

        self.content = self.card

    def show_delete_button(self, e):
        if e.data == "true":
            self.delete_button.visible = True
            self.delete_button.update()
        else:
            self.delete_button.visible = False
            self.delete_button.update()

    def build(self):
        return self.content
