from flet_core import UserControl
import flet as ft

from src.connections.client_conn import ClientConn
from src.data.items.card import CardData
from src.gui.controls.general.add_button import AddButton
from src.gui.controls.main_view.vault.cards.card_form import CardForm
from src.gui.controls.main_view.vault.cards.card_view import CardView


class CardsControl(UserControl):

    def __init__(self):
        super().__init__()
        self.expand = True
        self.content = None
        self.init()

    def init(self):
        self.card_form = CardForm(add_card=self.add_card)
        self.add_button = AddButton()
        self.add_button.button.on_click = self.card_form.open_dlg

        self.cards = ft.GridView(
            expand=1,
            runs_count=3,
            child_aspect_ratio=1.67,
            width=970,
            padding=ft.padding.all(10),

        )

        self.view = ft.Container(
            ft.Column(controls=[
                ft.Row(controls=[
                    ft.Text("Cards: ", size=20),
                    self.add_button,
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=900),
                self.cards
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),padding=ft.padding.all(10)

        )

    def append_card(self, card: CardData):
        card_view = CardView(card, self.remove_card, self.edit_card)
        self.cards.controls.append(card_view)

    def add_card(self, card: CardData):
        ClientConn().add_card(card)
        self.update()

    def remove_card(self, card_view, card_data):
        ClientConn().delete_card(card_data)
        self.update()

    def edit_card(self, card: CardData):
        ClientConn().add_card(card)
        self.update()

    def before_update(self):
        self.cards.controls.clear()
        print("update cards")
        items = ClientConn().get_user_items()
        if items.get("card"):
            for card in items["card"]:
                self.append_card(CardData(**card))

    def build(self):
        return self.view

