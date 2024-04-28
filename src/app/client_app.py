import flet as ft

from flet_core import UserControl

from src.connections.client_conn import ClientConn
from src.gui.Data import Data
from src.gui.controls.main_view.app_bar import MainBar
from src.gui.controls.index_view.index import IndexControl
from src.gui.controls.index_view.login_control import LoginControl
from src.gui.controls.index_view.register_control import RegisterControl


class App(UserControl):
    def __init__(self):
        super().__init__()
        self.data = dict()
        self.routes = {}
        self.body = ft.Container(alignment=ft.alignment.center, expand=True)
        self.conn = ClientConn("127.0.0.1", 1231)

        self.index_view = IndexControl()
        self.register_view = RegisterControl()
        self.login_view = LoginControl()

    def init(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = "light"
        self.page.appbar = MainBar(self.page)
        self.page.on_route_change = self.route_change
        self.page.padding = 0
        self.page.add(
            self.body
        )
        self.page.go('/')

        self.routes = {
            "/": self.index_view,
            "/register": self.register_view,
            "/login": self.login_view,
        }
        self.conn.main()

        self.register_view.login_button.on_click = self.register
        self.login_view.login_button.on_click = self.login

    def register(self, e):
        mail = self.register_view.mail_field.value
        username = self.register_view.username_field.value
        password = self.register_view.password_field.value
        self.conn.register(username, password, mail)
        self.page.go('/')

    def login(self, e):
        username = self.login_view.username_field.value
        password = self.login_view.password_field.value
        status = self.conn.login(username, password)
        if status:
            Data("username", username)

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
