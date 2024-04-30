import flet as ft


class SecurityContainer(ft.Container):
    def __init__(self, title, subtitle, icon, on_click):
        super().__init__()

        self.icon = icon
        self.title_label = ft.Text(title, size=20, weight=ft.FontWeight.BOLD)
        self.sub_title_label = ft.Text(subtitle, size=15)

        self.content = ft.Container(content=
        ft.Row([
            ft.Row(
                [
                    self.icon,

                    ft.Container(
                        ft.Column([
                            self.title_label,
                            self.sub_title_label
                        ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER)
                    )
                ]),
            ft.Icon(ft.icons.CHEVRON_RIGHT, color=ft.colors.GREY_800, size=50)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            alignment=ft.alignment.center,
            height=80,
            border_radius=10,
            ink=True,
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            on_click=on_click,

        )

    def build(self):
        return self.content
