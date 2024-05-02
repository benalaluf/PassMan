import flet as ft

from flet_core import UserControl, Theme

from src.connections.client_conn import ClientConn
from src.gui.views.index_view import IndexView
from src.gui.views.main_view import MainView


class App(UserControl):
    def __init__(self, *args, **kwargs):
        self.data = dict()
        self.routes = {}

        self.index_view = IndexView()
        self.main_view = MainView()

        self.conn = ClientConn()

        self.user_data = None

    def main(self, ip, port):
        self.init_conn(ip, port)
        ft.app(target=self.init_gui)

    def init_gui(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.theme_mode = "light"
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop

        self.custom_theme = Theme()
        self.custom_theme.color_scheme = ft.ColorScheme(tertiary=ft.colors.WHITE,
                                                        tertiary_container=ft.colors.BLACK,
                                                        on_tertiary=ft.colors.BLACK,
                                                        on_tertiary_container=ft.colors.BLACK
                                                        )
        self.custom_theme.page_transitions.linux = ft.PageTransitionTheme.CUPERTINO
        self.custom_theme.dialog_theme = ft.DialogTheme(bgcolor=ft.colors.BACKGROUND,
                                                        surface_tint_color=ft.colors.BACKGROUND)
        self.page.theme = self.custom_theme

        self.page.go('/')

        self.routes = {
            "/": self.index_view.index_control,
            "/register": self.index_view.register_control,
            "/login": self.index_view.login_control,
            "/2fa": self.index_view.two_fa_Control,
            "/main/vault": self.main_view.vault_control,
            "/main/vault/passwords": self.main_view.vault_control.passwords_control,
            "/main/vault/cards": self.main_view.vault_control.cards_control,
            "/main/security": self.main_view.security_control,
            "/main/security/2fa": self.main_view.security_control.enable_two_fa,
            "/main/security/password_breach": self.main_view.security_control.data_breach_checker_control,
            "/main/security/password_generator": self.main_view.security_control.password_genarator,
            "/main/settings": self.main_view.settings_control
        }

        self.index_view.register_control.login_button.on_click = self.register
        self.index_view.login_control.login_button.on_click = self.login
        self.index_view.two_fa_Control.login_button.on_click = self.two_fa
        self.main_view.settings_control.button.on_click = self.changethememode

        self.page.update()

    def init_conn(self, ip, port):
        self.conn.connect_to_server(ip, port)

    def route_change(self, route):
        print(route.route)

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

    def register(self, e):
        mail = self.index_view.register_control.mail_field.value
        username = self.index_view.register_control.username_field.value
        password = self.index_view.register_control.password_field.value
        status = self.conn.register(username, password, mail)
        if status:
            self.page.go('/main/vault/passwords')
            self.main_view.update_view(None)
        else:
            self.index_view.register_control.failed_login()

    def login(self, e):
        username = self.index_view.login_control.username_field.value
        password = self.index_view.login_control.password_field.value
        status = self.conn.login(username, password)
        if status == "Success":
            self.page.go('/main/vault/passwords')
            user_items = self.conn.get_user_items()
            self.main_view.update_view(user_items)
        if status == "2fa":
            self.page.go('/2fa')
        if status== "Fail":
            self.index_view.login_control.failed_login()


    def changethememode(self, e):
        # self.page.splash.visible = True
        self.page.theme_mode = "dark" if self.page.theme_mode == "light" else "light"
        self.page.update()

    def two_fa(self, e):
        conn = ClientConn()
        result = conn.two_fa(self.index_view.two_fa_Control.code_field.value)

        if result == "Success":
            print("OTP is valid")
            self.page.go('/main/vault/passwords')
            user_items = self.conn.get_user_items()
            self.main_view.update_view(user_items)
        print(result)

    def set_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        return self.data.get(key)

    def get_query(self, key):
        return self.data.get(key)


if __name__ == '__main__':
    app = App()
    app.main("127.0.0.1", 8080)
