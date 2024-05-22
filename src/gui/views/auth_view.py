from flet_core import View
import flet as ft

from src.gui.controls.index_view.app_bar import IndexBar
from src.gui.controls.auth_view.two_fa_control import TwoFAControl
from src.gui.controls.auth_view.login_control import LoginControl
from src.gui.controls.auth_view.register_control import RegisterControl


class AuthView(View):
    def __init__(self):
        super().__init__()
        self.body = ft.Container(alignment=ft.alignment.center, expand=True)
        self.padding = 0
        self.appbar = IndexBar(self.page)
        self.controls = [
            self.body
        ]
        self.register_control = RegisterControl()
        self.login_control = LoginControl()
        self.two_fa_Control = TwoFAControl()

