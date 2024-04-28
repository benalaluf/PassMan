from flet_core import NavigationBar, CupertinoNavigationBar, UserControl
import flet as ft


class MainNavMenu(NavigationBar):

    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__()
        self.page = page
        self.destinations = [
            ft.NavigationDestination(icon=ft.icons.DATA_OBJECT, label="Vault"),
            ft.NavigationDestination(icon=ft.icons.SHIELD, label="Security"),
            ft.NavigationDestination(
                icon=ft.icons.SETTINGS,
                label="Settings",
            )
        ]
        self.height = 80
        self.bgcolor = ft.colors.WHITE
        self.elevation = 3
        self.on_change = self.route
        self.disabled = False

    def route(self,e):
        print("Selected destination:", e.control.selected_index)
        if e.control.selected_index == 0:
            self.page.go('/main/vault/passwords')
        elif e.control.selected_index == 1:
            self.page.go('/main/security')
        elif e.control.selected_index == 2:
            self.page.go('/main/settings')
        else:
            print("Invalid destination")
        self.page.update()





