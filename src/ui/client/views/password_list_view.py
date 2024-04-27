import flet as ft
from flet_core import UserControl


class PasswordListView(UserControl):
    def __init__(self, passwords):
        super().__init__()
        self.passwords = passwords
        self.password_list = ft.ListView()
        self.content = ft.Column(
            controls=[
                ft.Text("Saved Passwords"),
                self.password_list
            ],
            alignment=ft.alignment.center,
        )

    def init(self, page: ft.Page):
        self.page = page
        self.page.add(self.content)
        self.update_password_list()

    def update_password_list(self):
        self.password_list.children = [self.create_password_item(password) for password in self.passwords]

    def create_password_item(self, password):
        item = ft.ListTile(text=password['site'])
        item.on_click = lambda e: self.show_password_details(password)
        return item

    def show_password_details(self, password):
        details = f"""
        Site: {password['site']}
        Username: {password['username']}
        Password: {password['password']}
        Date: {password['date']}
        Notes: {password['notes']}
        """
        ft.AlertDialog().show()
