import flet as ft


class SettingsButton(ft.Container):
    def __init__(self, title, on_click):
        super().__init__()
        self.on_click = on_click

        self.title_label = ft.Text(title, size=20, weight=ft.FontWeight.BOLD)

        self.content = ft.Container(content=
        ft.Row([
            self.title_label,
            ft.Icon(ft.icons.CHEVRON_RIGHT, color=ft.colors.ON_SURFACE_VARIANT, size=50)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            alignment=ft.alignment.center,
            height=60,
            border_radius=10,
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            padding=ft.Padding(20, 0, 20, 0),
            on_click=self.on_click,
            ink=True

        )

    def build(self):
        return self.content
