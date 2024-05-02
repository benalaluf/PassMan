from flet_core import NavigationBar, CupertinoNavigationBar, UserControl
import flet as ft


class MainNavMenu(NavigationBar):

    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__()
        self.page = page
        self.destinations = [
            ft.NavigationDestination(icon=ft.icons.ACCOUNT_BALANCE_WALLET, label="Vault"),
            ft.NavigationDestination(icon=ft.icons.SHIELD, label="Security"),
            ft.NavigationDestination(
                icon=ft.icons.SETTINGS,
                label="Settings",
            )
        ]
        self.height = 80
        self.surface_tint_color = ft.colors.BLUE_GREY
        self.elevation = 3
        self.indicator_color = ft.colors.RED
        self.on_change = self.route
        self.disabled = False

    def route(self,e):
        if e.control.selected_index == 0:
            self.page.go('/main/vault/passwords')
        elif e.control.selected_index == 1:
            self.page.go('/main/security')
        elif e.control.selected_index == 2:
            self.page.go('/main/settings')
        else:
            print("Invalid destination")
        self.page.update()





