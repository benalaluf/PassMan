import flet as ft
from flet_core import UserControl

from src.gui.controls.indevelopment import InDevelopmentControl
from src.gui.controls.main_view.vault.cards.cards_control import CardsControl
from src.gui.controls.main_view.vault.passwords.password_control import PasswordControl
from src.gui.controls.main_view.vault.vault_navigation import VaultNavigationRail





class VaultControl(UserControl):
    def __init__(self):
        super().__init__()
        self.expand= True
        self.body = ft.Container(alignment=ft.alignment.center, expand=True, padding=0)
        self.content = ft.Row(
            [
                VaultNavigationRail(self.page),
                self.body

            ],
            spacing=0
        )
        self.passwords_control = PasswordControl()
        self.cards_control = CardsControl()
        self.notes_control = InDevelopmentControl()
        self.contacts_control = InDevelopmentControl()

    def build(self):
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()
