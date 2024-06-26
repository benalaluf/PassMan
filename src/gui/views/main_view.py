from flet_core import View, AppBar
import flet as ft

from src.connections.client_conn import ClientConn
from src.data.db.card import CardData
from src.data.db.password import PasswordData
from src.gui.controls.indevelopment import InDevelopmentControl
from src.gui.controls.main_view.app_bar import MainBar
from src.gui.controls.main_view.main_nav import MainNavMenu
from src.gui.controls.main_view.security.security_control import SecurityControl
from src.gui.controls.main_view.setttings.settings_control import SettingsControl
from src.gui.controls.main_view.vault.vault_control import VaultControl


class MainView(View):
    def __init__(self):
        super().__init__()
        self.body = ft.Container(alignment=ft.alignment.center, expand=True)
        self.padding = 0
        self.main_bar =MainBar(self.page)
        self.appbar = self.main_bar
        self.navigation_bar = MainNavMenu(self.page)
        self.controls = [
            self.body
        ]
        self.vault_control = VaultControl()
        self.security_control = SecurityControl()
        self.settings_control = SettingsControl()



    def update_view(self, items):
        pass
        # if db:
        #     print(db)
        #     passwords = db.get('password')
        #     cards = db.get('card')
        #     if passwords:
        #         for password in passwords:
        #             self.vault_control.passwords_control.append_password(PasswordData(**password))
        #     if cards:
        #         for card in cards:
        #             self.vault_control.cards_control.append_card(CardData(**card))
        #
        #
        #     if cards:
        #         pass






