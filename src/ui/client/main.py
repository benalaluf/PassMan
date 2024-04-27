from flet_core import UserControl, View
import flet as ft

from src.ui.client.controls.app_bar import NavBar
from src.ui.client.views.data_view import DataView
from src.ui.client.views.index_view import IndexView
from src.ui.client.views.login_view import LoginView
from src.ui.client.views.register_view import RegisterView


class App(UserControl):
    def __init__(self):
        super().__init__()
        self.data = dict()
        self.routes = {}
        self.body = ft.Container(alignment=ft.alignment.center, expand=True)

        self.index_view = IndexView()
        self.register_view = RegisterView()
        self.login_view = LoginView()
        self.data_view = DataView()

    def init(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.theme_mode = "light"
        self.page.appbar = NavBar(self.page)
        self.page.on_route_change = self.route_change
        self.page.add(
            self.body
        )
        self.page.go('/')

        self.routes = {
            "/": self.index_view,
            "/register": self.register_view,
            "/login": self.login_view,
            "/data": self.data_view,
        }

        self.register_view.login_button.on_click = self.register
        self.login_view.login_button.on_click = self.login

    def register(self, e):
        mail = self.register_view.mail_field.value
        username = self.register_view.username_field.value
        password = self.register_view.password_field.value
        self.page.go('/')

    def login(self, e):
        username = self.login_view.username_field.value
        password = self.login_view.password_field.value
        self.page.go('/')

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()

    def set_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        return self.data.get(key)

    def get_query(self, key):
        return self.data.get(key)


if __name__ == '__main__':
    app = App()
    ft.app(target=app.init)
