import flet as ft

from flet_core import UserControl

from src.ui.client.controls.app_bar import NavBar
from src.ui.client.views.data_view import DataView
from src.ui.client.views.index_view import IndexView
from src.ui.client.views.login_view import LoginView
from src.ui.client.views.register_view import RegisterView


class App(UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.data = dict()
        self.routes = {}
        self.body = ft.Container(alignment=ft.alignment.center)
        self.init()

    def init(self):
        self.page.theme_mode = "light"
        self.page.appbar = NavBar(self.page)
        self.page.on_route_change = self.route_change
        self.page.add(
            self.body
        )
        self.page.go('/')

        self.routes = {
            "/": IndexView(),
            "/register": RegisterView(),
            "/login": LoginView(),
             "/data": DataView(),
        }

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
    ft.app(target=App)
