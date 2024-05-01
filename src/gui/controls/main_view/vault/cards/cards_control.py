from flet_core import UserControl, ListView
import flet as ft

from src.connections.client_conn import ClientConn
from src.data.items.card import CardData
from src.data.items.password import PasswordData
from src.gui.controls.main_view.vault.cards.card_view import CardView
from src.gui.controls.main_view.vault.passwords.password_add_button import PasswordAddButton
from src.gui.controls.main_view.vault.passwords.password_container import PasswordContainer
from src.gui.controls.main_view.vault.passwords.password_form_dialog import PasswordFormDialog


class CardsControl(UserControl):

    def __init__(self):
        super().__init__()
        self.content = None
        self.init()

    def init(self):
        self.cards = ft.GridView(
            runs_count=3,
            child_aspect_ratio=1.67,
            width=970,
            padding=ft.padding.all(10)
        )

        self.cards.scroll = ft.ScrollMode.ALWAYS

        self.cards.controls.append(CardView(CardData("Mastercard", "1234 5678 9101 1121","123", "12/23")))
        self.cards.controls.append(CardView(CardData("Mastercard", "1234 5678 9101 1121","123", "12/23")))
        self.cards.controls.append(CardView(CardData("Mastercard", "1234 5678 9101 1121","123", "12/23")))
        self.cards.controls.append(CardView(CardData("Mastercard", "1234 5678 9101 1121","123", "12/23")))

        self.cards_container = ft.Container(
            self.cards,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLUE,
        )

        self.add_button = ft.ElevatedButton("Add", ft.icons.ADD, color=ft.colors.RED)


        self.view = ft.Container(
            ft.Column(controls=[
                ft.Row(controls=[
                    ft.Text("Cards: ", size=20),
                    self.add_button,
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=930),
                self.cards_container
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )


    def build(self):
        print("nigger the nigger")
        return self.view
