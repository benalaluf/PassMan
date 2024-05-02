import flet as ft
from flet_core import UserControl

from src.password_strenght.password_data_breach import check_pwned_password
from src.password_strenght.passwrod_genarator import generate_password


class PasswordGenerator(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.content = None
        self.init()

    def init(self):
        self.title = ft.Text("Password Generator", size=40, )

        self.password_field = ft.Text(size=25, weight=ft.FontWeight.BOLD, )

        self.generate_button = ft.ElevatedButton(text="Generate", width=200)
        self.generate_button.on_click = self.genarate_button_clicked

        self.copy_button = ft.IconButton(icon=ft.icons.COPY, icon_size=30)

        self.title_container = ft.Container(
            self.title,
            alignment=ft.alignment.center,
        )
        self.password_hint = ft.Text("Click on the password to copy!", size=15)
        self.password_hint.visible = False
        self.password_field_container = ft.Container(
            self.password_field,
            on_click=lambda _: self.page.set_clipboard(self.password_field.value),
            ink=True,

        )
        self.generate_view = ft.Container(
            ft.Column(
                [
                    self.password_field_container,
                    self.password_hint,
                    self.generate_button
                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

        self.content = ft.Container(
            ft.Container(
                ft.Column(
                    controls=[
                        self.title_container,
                        self.generate_view,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=100
                ),
                border_radius=14,
                bgcolor=ft.colors.BACKGROUND,
                border=ft.border.all(color=ft.colors.BLACK, width=2),
                height=500,
                width=500,
            ),
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.GREY_700
        )

    def genarate_button_clicked(self, e):
        result = generate_password(16)
        self.password_field.value = result
        self.password_hint.visible = True


        self.update()

    def build(self):
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()
