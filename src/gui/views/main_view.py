from flet_core import View, AppBar
import flet as ft
from src.gui.controls.main_view.app_bar import MainBar
from src.gui.controls.main_view.nav_menu import MainNavMenu
from src.gui.controls.main_view.vault.vault_control import VaultControl


class MainView(View):
    def __init__(self):
        super().__init__()
        self.body = ft.Container(alignment=ft.alignment.center, expand=True)
        self.padding = 0
        self.appbar = MainBar(self.page)
        self.navigation_bar = MainNavMenu(self.page)
        self.controls = [
            self.body
        ]
        self.vault_control = VaultControl()

