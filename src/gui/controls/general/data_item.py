import flet as ft


class DataItemControl(ft.UserControl):

    def __init__(self, title, data):
        super().__init__()
        self.title = title
        self.data = data
        self.init()

    def init(self):
        self.title_lable = ft.Text(self.title, size=15, weight=ft.FontWeight.W_500)

        self.data_lable = ft.Text(self.data, size=20, weight=ft.FontWeight.BOLD)

        self.data_row_lable = ft.Row(controls=[
            self.data_lable,
            ft.IconButton(ft.icons.COPY, icon_size=20, icon_color=ft.colors.BLUE, on_click=lambda _:self.page.set_clipboard(self.data))
            ]
        )
        self.data_field = ft.TextField(value=self.data, text_size=20,
                                       border=ft.InputBorder.UNDERLINE)
        self.data_field.visible = False

        self.content = ft.Container(
            ft.Column(controls=[
                self.title_lable,
                self.data_field,
                self.data_row_lable,
            ], spacing=0),
        )

    def build(self):
        return self.content

    def edit(self):
        self.data_row_lable.visible = False
        self.data_field.visible = True
        self.update()

    def view(self):
        self.data_row_lable.visible = True
        self.data_field.visible = False
        self.update()
