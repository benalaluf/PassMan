import flet as ft
from flet_core import UserControl

from src.password_strenght.password_data_breach import check_pwned_password


class PasswordDataBreach(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.content = None
        self.init()

    def init(self):
        self.title = ft.Text("Password Data-Breach Checker", size=40, )
        self.password_field = ft.TextField(
            hint_text="Password",
            text_size=30,
            border=ft.InputBorder.UNDERLINE,
            text_align=ft.TextAlign.CENTER,
        )
        self.check_button = ft.ElevatedButton(text="Check", width=200)
        self.check_button.on_click = self.check_button_clicked
        self.checker = ft.Container(
            ft.Column(
            [
                self.password_field,
                self.check_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.Padding(300, 0, 300, 0),
        )

        self.result_text = ft.Text(size=30, weight=ft.FontWeight.BOLD)
        self.green_icon = ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN, size=50)
        self.yellow_icon = ft.Icon(ft.icons.WARNING, color=ft.colors.YELLOW_800, size=50)

        self.red_icon = self.result_icon = ft.Icon(ft.icons.ERROR, color=ft.colors.RED, size=50)

        self.green_icon.visible = False
        self.yellow_icon.visible = False
        self.red_icon.visible = False
        self.result_text.visible = False
        self.result_display = ft.Container(
            ft.Column(controls=[
                self.green_icon,
                self.yellow_icon,
                self.red_icon,
                self.result_text,
            ]),
            alignment=ft.alignment.center,
        )
        self.view = ft.Container(
            ft.Container(
                ft.Column(
                    controls=[self.title,self.checker, self.result_display],
                    spacing=30,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                expand=True,
                border_radius=14,
                bgcolor=ft.colors.GREY_100,
                padding=20,
                margin=ft.Margin(100,20,100,20),
                border=ft.border.all(color=ft.colors.BLACK, width=2),
            ),
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.GREY_700
        )
        self.content = ft.Container(
            self.view,
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.GREY_700
        )

    def check_button_clicked(self, e):
        result = check_pwned_password(self.password_field.value)
        if result == 0:
            self.yellow_icon.visible = False
            self.green_icon.visible = True
            self.red_icon.visible = False
            self.result_text.value = "No Data Breach found, Password is secure"
            self.result_text.color = ft.colors.GREEN
        if 0 < result < 50:
            self.yellow_icon.visible = True
            self.green_icon.visible = False
            self.red_icon.visible = False
            self.result_text.value = f"{result} Data Breach found, Password is weak"
            self.result_text.color = ft.colors.YELLOW_800

        if result > 50:
            self.yellow_icon.visible = False
            self.green_icon.visible = False
            self.red_icon.visible = True
            self.result_text.value = f"{result} Data Breach found, Password is compromised"
            self.result_text.color = ft.colors.RED

        self.result_text.visible = True

        self.update()

    def build(self):
        return self.content

    def exit_app(self, e):
        page = e.page
        page.window_destroy()
