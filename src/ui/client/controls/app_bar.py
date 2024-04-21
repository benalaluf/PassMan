import flet as ft
from flet_core import UserControl, AppBar


class NavBar(AppBar):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.nav_drawer = ft.NavigationDrawer()
        self.menu_button = ft.IconButton()
        self.page.drawer = self.nav_drawer
        self.init()

    def init(self):
        self.menu_button.icon = ft.icons.MENU
        self.menu_button.on_click = self.open_drawer
        self.menu_button.icon_color = ft.colors.WHITE

        self.leading = self.menu_button
        self.leading_width = 50
        self.title = ft.Text("PassMan", color='white')
        self.center_title = False
        self.bgcolor = ft.colors.RED
        self.actions = [
            ft.IconButton(ft.icons.HOME, icon_color='white', on_click=lambda _: self.page.go('/')),
            ft.ElevatedButton(text="Login", color="red", on_click=lambda _: self.page.go('/login')),
            ft.ElevatedButton(text="Register", color="red", on_click=lambda _: self.page.go('/register'))
        ]

        self.nav_drawer.controls = [
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.icons.PHONE,
            ),
        ]
        self.nav_drawer.on_change = self.close_drawer

    def open_drawer(self, e):
        self.page.drawer.open = True
        self.page.drawer.update()

    def close_drawer(self, e):
        self.nav_drawer.open = False
        self.nav_drawer.update()
