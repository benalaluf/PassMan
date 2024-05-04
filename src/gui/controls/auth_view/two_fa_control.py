import flet as ft

from src.connections.client_conn import ClientConn
from src.crypto.two_fa import verify_otp


class TwoFAControl(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.title = ft.Text("2FA", size=40, color=ft.colors.BLACK)
        self.code_field = ft.TextField(hint_text="Code",
                                       border=ft.InputBorder.UNDERLINE,
                                       label="Code",
                                       text_align=ft.TextAlign.CENTER,
                                       text_size=20,
                                       color=ft.colors.BLACK,
                                       on_change=self.code_field_on_change)
        self.login_button = ft.ElevatedButton(text="Login", width=200)
        self.login_button.on_click = self.two_fa
        self.code_field.input_filter = ft.InputFilter(r'[0-9]')

        self.code_field.show_cursor = False

        self.login = ft.Container(ft.Column(
            [
                self.title,
                self.code_field,
                self.login_button
            ],
            width=400,
            height=400,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            border_radius=14,
            bgcolor=ft.colors.WHITE,
            padding=20,
            border=ft.border.all(color=ft.colors.BLACK, width=2),
        )

        self.content = ft.Container(
            self.login,
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.GREY_700
        )

    def two_fa(self, e):
        print("2FA")
        conn = ClientConn()
        result = conn.two_fa(self.code_field.value)
        print(result)
        if result == "Success":
            print("OTP is valid")
            self.page.go('/main/vault/passwords')
        else:
            self.on_fail()

        print(result)

    def code_field_on_change(self, e):
        self.code_field.error_text = ""
        self.code_field.update()

    def on_fail(self):
        self.code_field.error_text = "Invalid Code!"
        self.code_field.update()

    def build(self):
        return self.content


if __name__ == '__main__':
    def main(page: ft.Page):
        page.add(TwoFAControl())


    ft.app(target=main)
