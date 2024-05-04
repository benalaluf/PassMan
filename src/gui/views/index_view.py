from flet_core import View
import flet as ft

from src.gui.controls.index_view.app_bar import IndexBar
from src.gui.controls.index_view.index import IndexControl


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

