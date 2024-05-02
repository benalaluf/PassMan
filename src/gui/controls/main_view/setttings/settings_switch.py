import flet as ft

class SettingsSwitch(ft.Container):
    def __init__(self, title, on_change):
        super().__init__()

        self.title_label = ft.Text(title, size=20, weight=ft.FontWeight.BOLD)
        self.switch = ft.Switch(value=False)
        self.switch.on_change = on_change


        self.content = ft.Container(content=
        ft.Row([
            self.title_label,
            self.switch,

        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            alignment=ft.alignment.center,
            height=60,
            border_radius=10,
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            padding=ft.Padding(20,0,20,0),

        )

    def build(self):
        return self.content