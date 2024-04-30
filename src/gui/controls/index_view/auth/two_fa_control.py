import flet as ft


class TwoFAControl(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.title = ft.Text("2FA", size=40, color=ft.colors.BLACK )
        self.code_field = ft.TextField(hint_text="Code",
                                       border=ft.InputBorder.UNDERLINE,
                                       label="Code",
                                       text_align=ft.TextAlign.CENTER,
                                       text_size=20,
                                       color=ft.colors.BLACK,)
        self.login_button = ft.ElevatedButton(text="Login", width=200)
        self.code_field.input_filter = ft.InputFilter(r'[0-9]')

        self.code_field.show_cursor = False



        self.login_button.on_click = self.login

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

    def login(self, e):
        self.code_field.error_text = "Invalid code"
        self.update()
    def build(self):
        return self.content






if __name__ == '__main__':
    def main(page: ft.Page):
        page.add(TwoFAControl())

    ft.app(target=main)
