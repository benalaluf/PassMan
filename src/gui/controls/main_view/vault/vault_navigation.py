from flet_core import NavigationRail, UserControl
import flet as ft


class VaultNavigationRail(UserControl):

    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.content = None
        self.init()

    def init(self):
        self.rail = ft.Container(
            ft.Column(

                controls=[
                    ft.Container(
                        content=ft.Column(controls=[ft.Icon(name=ft.icons.KEY, color=ft.colors.GREY_800), ft.Text("Passwords")],
                                          alignment=ft.MainAxisAlignment.CENTER,
                                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                          spacing=0),

                        alignment=ft.alignment.center,
                        height=80,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _:self.page.go('/main/vault/passwords',
                    ),
                    ),
                    ft.Container(
                        content=ft.Column(controls=[ft.Icon(name=ft.icons.CREDIT_CARD_ROUNDED, color=ft.colors.GREY_800), ft.Text("Cards")],
                                          alignment=ft.MainAxisAlignment.CENTER,
                                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                          spacing=0),
                        alignment=ft.alignment.center,
                        height=80,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _: self.page.go("/main/vault/cards")
                    ),
                    ft.Container(
                        content=ft.Column(controls=[ft.Icon(name=ft.icons.EDIT_NOTE_ROUNDED     , color=ft.colors.GREY_800), ft.Text("Notes")],
                                          alignment=ft.MainAxisAlignment.CENTER,
                                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                          spacing=0),
                        alignment=ft.alignment.center,
                        height=80,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _: self.page.go("/main/vault/notes")
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[ft.Icon(name=ft.icons.CONTACTS, color=ft.colors.GREY_800), ft.Text("contacts")],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0),
                        alignment=ft.alignment.center,
                        height=80,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _: self.page.go("/main/vault/contacts")

                    ),

                ],
                width=130, alignment=ft.MainAxisAlignment.START, spacing=10), )

        self.content = ft.Row([self.rail, ft.VerticalDivider(width=1)], spacing=0)

    def build(self):
        return self.content
