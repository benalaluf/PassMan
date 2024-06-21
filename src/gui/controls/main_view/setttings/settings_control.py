import flet as ft
from flet_core import UserControl

from src.connections.client_conn import ClientConn
from src.gui.controls.main_view.setttings.settings_button import SettingsButton
from src.gui.controls.main_view.setttings.settings_switch import SettingsSwitch


class SettingsControl(UserControl):

    def __init__(self):
        super().__init__()
        self.button = ft.IconButton(ft.icons.DARK_MODE)

        self.enable_dark_mode = SettingsSwitch("Enable Dark Mode", self.theme_changed)
        self.export_password = SettingsButton("Export Password", self.export_password)

        self.options = ft.Container(
            ft.Column(
                controls=[
                    self.enable_dark_mode,
                    # self.export_password
                ],
                expand=True,
                spacing=5,
            ),
            padding=ft.Padding(50, 0, 50, 0),
        )
        self.content = ft.Column(
            [
                ft.Text("Settings", size=40, weight=ft.FontWeight.BOLD),
                self.options,

            ]
            , horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=50,
        )

    def theme_changed(self, e):
        e.control.page.theme_mode = (
            ft.ThemeMode.LIGHT
            if e.control.page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        e.control.page.update()

    def export_password(self, e):
        print("in development")

    def clear_clipboard(self, e):
        self.page.set_clipboard("")

    def build(self):
        return self.content
