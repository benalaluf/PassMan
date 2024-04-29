from flet_core import UserControl, Theme
import flet as ft

from src.gui.views.index_view import IndexView
from src.gui.views.main_view import MainView


class App(UserControl):
    def __init__(self):
        super().__init__()
        self.data = dict()
        self.routes = {}

        self.index_view = IndexView()
        self.main_view = MainView()

    def init(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.theme_mode = "light"
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop

        theme = Theme()
        theme.color_scheme = ft.ColorScheme(surface_tint=ft.colors.WHITE,)
        theme.page_transitions.linux = ft.PageTransitionTheme.CUPERTINO
        theme.color_scheme.surface_tint = ft.colors.WHITE
        self.page.theme = theme

        self.page.go('/')

        self.routes = {
            "/": self.index_view.index_control,
            "/register": self.index_view.register_control,
            "/login": self.index_view.login_control,
            "/main/vault": self.main_view.vault_control,
            "/main/vault/passwords": self.main_view.vault_control.passwords_control,
            "/main/vault/cards": self.main_view.vault_control.cards_control,
            "/main/security": self.main_view.security_control,
            "/main/settings": self.main_view.settings_control
        }

        self.index_view.register_control.login_button.on_click = self.register
        self.index_view.login_control.login_button.on_click = self.login

        self.page.update()

    def register(self, e):
        mail = self.index_view.register_control.mail_field.value
        username = self.index_view.register_control.username_field.value
        password = self.index_view.register_control.password_field.value
        self.page.go('/main/vault/passwords')

    def login(self, e):
        username = self.index_view.login_control.username_field.value
        password = self.index_view.login_control.password_field.value

        self.page.go('/main/vault/passwords')

    def route_change(self, route):
        if not route.route.startswith("/main"):
            self.index_view.body.content = self.routes[route.route]

            if self.page.views[0] is not self.index_view:
                self.page.views.clear()
                self.page.views.append(self.index_view)
        else:
            if route.route != "/main":
                if self.page.views[0] is not self.main_view:
                    self.page.views.clear()
                    self.page.views.append(self.main_view)

                if route.route.split("/")[2] == "vault":
                    self.main_view.vault_control.body.content = self.routes[route.route]
                    self.main_view.body.content = self.main_view.vault_control
                    self.page.update()
                else:
                    self.main_view.body.content = self.routes[route.route]

        self.page.update()
        print(route.route)

    def view_pop(self, e):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    def set_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        return self.data.get(key)

    def get_query(self, key):
        return self.data.get(key)


if __name__ == '__main__':
    app = App()
    ft.app(target=app.init)
