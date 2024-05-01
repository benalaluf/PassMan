from flet_core import UserControl

from src.connections.client_conn import ClientConn
from src.data.items.card import CardData
from src.data.items.password import PasswordData
import flet as ft

from src.gui.controls.main_view.vault.passwords.password_data_dialog import PasswordDataDialog
from src.gui.controls.main_view.vault.passwords.password_form_dialog import PasswordFormDialog


class CardView(UserControl):
    def __init__(self, card_data: CardData):
        super().__init__()
        self.card_data = card_data

        self.init()

    def init(self):
        self.menu_button = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(icon=ft.icons.EDIT),
                ft.PopupMenuItem(icon=ft.icons.DELETE),
                ft.PopupMenuItem(icon=ft.icons.COPY)
            ]
        )
        self.bank_name_label = ft.Text(self.card_data.bank_name, size=20, weight=ft.FontWeight.BOLD)
        self.card_number_label = ft.Text(
            "**** **** **** "+ self.card_data.card_number[-4:],
            size=20,
            weight=ft.FontWeight.BOLD
        )
        self.img = ft.Icon(
            ft.icons.CREDIT_CARD,
            size=60,
            color=ft.colors.OUTLINE_VARIANT
        )

        self.CardTest = ft.Card(
            content=ft.Container(
                content=(
                    ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Column(
                                        spacing=1,
                                        controls=[
                                            ft.Container(
                                                alignment=ft.alignment.bottom_left,
                                                content=ft.Text(
                                                    'BANK NAME',
                                                    size=9,
                                                    weight=ft.FontWeight.W_500,
                                                ),
                                            ),
                                            ft.Container(
                                                alignment=ft.alignment.top_left,
                                                content=ft.Text(
                                                    self.card_data.bank_name,
                                                    size=20,
                                                    weight=ft.FontWeight.W_500,
                                                ),
                                            ),
                                        ],
                                    ),
                                    ft.Icon(
                                        name=ft.icons.SETTINGS_OUTLINED,
                                        size=16,
                                    ),
                                ],
                            ),
                            ft.Container(
                                padding=ft.padding.only(top=10, bottom=20),
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Column(
                                        spacing=1,
                                        controls=[
                                            ft.Container(
                                                alignment=ft.alignment.bottom_left,
                                                content=ft.Text(
                                                    'CARD NUMBER',
                                                    size=9,
                                                    weight=ft.FontWeight.W_500,
                                                ),
                                            ),
                                            ft.Container(
                                                alignment=ft.alignment.top_left,
                                                content=ft.Text(
                                                    f'**** **** **** {self.card_data.card_number[-4:]}',
                                                    size=15,
                                                    weight=ft.FontWeight.W_700,
                                                ),
                                                data=(
                                                   self.card_data.card_number),
                                            ),
                                            ft.Container(
                                                bgcolor='pink',
                                                padding=ft.padding.only(bottom=5),
                                            ),
                                            ft.Container(
                                                alignment=ft.alignment.bottom_left,
                                                content=ft.Text(
                                                    'CVV NUMBER',
                                                    size=9,
                                                    weight=ft.FontWeight.W_500,
                                                ),
                                            ),
                                            ft.Container(
                                                alignment=ft.alignment.top_left,
                                                content=ft.Text(
                                                    f'**{self.card_data.cvv[-1:]}',
                                                    size=13,
                                                    weight=ft.FontWeight.W_700,
                                                ),
                                                data=self.card_data.cvv,
                                            ),
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

            ),

            elevation=5
        )

        self.content = self.CardTest


    def build(self):
        return self.content
