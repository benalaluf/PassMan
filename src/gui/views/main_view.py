from flet_core import View, AppBar
import flet as ft
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
        self.appbar = MainBar(self.page)
        self.navigation_bar = MainNavMenu(self.page)
        self.controls = [
            self.body
        ]
        self.vault_control = VaultControl()
        self.security_control = SecurityControl()
        self.settings_control = SettingsControl()

