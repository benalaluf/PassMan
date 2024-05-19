from pathlib import Path

from flet_core import UserControl, Theme
import flet as ft

from src.gui.views.auth_view import AuthView
from src.gui.views.index_view import IndexView
from src.gui.views.main_view import MainView
from src.settings import THEME


class ClientGUI():
    def __init__(self):
        super().__init__()
        self.routes = {}

        self.index_view = IndexView()
        self.auth_view = AuthView()
        self.main_view = MainView()

    def main(self):
        ft.app(target=self.init_gui, assets_dir=str(Path(__file__).resolve().parent / "assets"))

    def init_gui(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.theme_mode = "light"
        self.page.window_width = 1200
        self.page.window_height = 800

        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop

        self.page.theme = THEME

        self.page.go('/')

        self.routes = {"/": self.index_view.index_control,
                       "/auth/register": self.auth_view.register_control,
                       "/auth/login": self.auth_view.login_control,
                       "/auth/2fa": self.auth_view.two_fa_Control,
                       "/main/vault": self.main_view.vault_control,
                       "/main/vault/passwords": self.main_view.vault_control.passwords_control,
                       "/main/vault/cards": self.main_view.vault_control.cards_control,
                       "/main/security": self.main_view.security_control,
                       "/main/security/2fa": self.main_view.security_control.enable_two_fa,
                       "/main/security/password_breach": self.main_view.security_control.data_breach_checker_control,
                       "/main/security/password_generator": self.main_view.security_control.password_genarator,
                       "/main/settings": self.main_view.settings_control}

        self.page.update()

    def route_change(self, route):
        print(route.route)
        if route.route == "/":
            self.index_view.body.content = self.routes[route.route]

            if self.page.views[0] is not self.index_view:
                self.page.views.clear()
                self.page.views.append(self.index_view)

        elif route.route.startswith("/auth"):
            self.auth_view.body.content = self.routes[route.route]

            if self.page.views[0] is not self.auth_view:
                self.page.views.clear()
                self.page.views.append(self.auth_view)

        elif route.route.startswith("/main"):
            if self.page.views[0] is not self.main_view:
                self.page.views.clear()
                self.page.views.append(self.main_view)

            if route.route.split("/")[2] == "vault":
                self.main_view.body.content = self.main_view.vault_control
                self.page.update()
                self.main_view.vault_control.body.content = self.routes[route.route]
                self.main_view.vault_control.body.update()
            else:
                self.main_view.body.content = self.routes[route.route]

        self.page.update()

    def view_pop(self, e):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


if __name__ == '__main__':
    app = ClientGUI().main()
