from flet_core import UserControl, Theme
import flet as ft

from src.gui.controls.main_view.app_bar import MainBar
from src.gui.controls.index_view.index import IndexControl
from src.gui.controls.index_view.login_control import LoginControl
from src.gui.controls.index_view.register_control import RegisterControl
from src.gui.controls.main_view.vault.vault_control import VaultControl
from src.gui.views.index_view import IndexView
from src.gui.views.main_view import MainView


class App(UserControl):
    def __init__(self):
        super().__init__()
        self.data = dict()
        self.routes = {}

        self.index_view = IndexView()
        self.main_view = MainView()

        self.index_control = IndexControl()
        self.register_control = RegisterControl()
        self.login_control = LoginControl()

        self.vault_control = VaultControl()

    def init(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.theme_mode = "light"
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop

        theme = Theme()
        theme.page_transitions.linux = ft.PageTransitionTheme.CUPERTINO

        self.page.theme = theme

        self.page.go('/')

        self.routes = {
            "/": self.index_control,
            "/register": self.register_control,
            "/login": self.login_control,
            "/main/vault": self.vault_control
        }

        self.register_control.login_button.on_click = self.register
        self.login_control.login_button.on_click = self.login

        self.page.update()

    def register(self, e):
        mail = self.register_control.mail_field.value
        username = self.register_control.username_field.value
        password = self.register_control.password_field.value
        self.page.go('/main')

    def login(self, e):
        username = self.login_control.username_field.value
        password = self.login_control.password_field.value
        self.page.go('/main')

    def route_change(self, route):
        if 'main' not in route.route :
            self.index_view.body.content = self.routes[route.route]

            if self.page.views[0] is not self.index_view:
                self.page.views.clear()
                self.page.views.append(self.index_view)
        else:

            if route.route != "/main":
                self.main_view.body.content = self.routes[route.route]
            if self.page.views[0] is not self.main_view:
                self.page.views.clear()
                self.page.views.append(self.main_view)

        self.page.update()
        print(route.route)
        print(self.page.views)


    def view_pop(self,e):
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
