from flet_core import UserControl, View
import flet as ft

from src.gui.controls.index_view.app_bar import IndexBar
from src.gui.controls.main_view.app_bar import MainBar
from src.gui.controls.index_view.index import IndexControl
from src.gui.controls.index_view.login_control import LoginControl
from src.gui.controls.index_view.register_control import RegisterControl


class IndexView(View):
    def __init__(self):
        super().__init__()
        self.body = ft.Container(alignment=ft.alignment.center, expand=True)
        self.padding = 0
        self.appbar = IndexBar(self.page)
        self.controls = [
            self.body
        ]
        self.index_control = IndexControl()
        self.register_control = RegisterControl()
        self.login_control = LoginControl()

