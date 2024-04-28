import flet as ft
from flet_core import UserControl

from src.gui.controls.main_view.vault.vault_nav import VaultNavigationRail


class VaultControl(UserControl):
    def __init__(self ):
        super().__init__()

        self.content = ft.Row(
            [
                VaultNavigationRail(self.page),
                ft.Text("Vault", size=50),

            ]
        )

    def build(self):
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()
