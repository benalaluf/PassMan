import flet as ft


class DateDropDown(ft.UserControl):

    def __init__(self, year_from, year_to):
        super().__init__()
        self.year_from = year_from
        self.year_to = year_to
        self.init()

    def init(self):
        self.year_options = [ft.dropdown.Option(str(x)) for x in range(self.year_from, self.year_to+1)]
        self.month_options = [ft.dropdown.Option(str(x)) for x in range(1, 13)]

        self.year = ft.Dropdown(
            width=70,
            options=self.year_options,
            hint_text="YY"
        )
        self.month = ft.Dropdown(
            width=70,
            options=self.month_options,
            hint_text="MM"
        )

        self.content = ft.Container(
            ft.Row(
                controls=[
                    ft.Icon(ft.icons.CALENDAR_MONTH),
                    ft.Container(padding=ft.Padding(10, 0, 0, 0)),
                    self.year,
                    self.month,
                ],
                spacing=0
            ),
            alignment=ft.alignment.center
        )

    def get_data(self):
        return "{}/{}".format(self.month.value, self.year.value)
    def clear_data(self):
        self.month.value = ''
        self.year.value = ''

    def build(self):
        return self.content


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(DateDropDown(20, 30))
        page.update()


    ft.app(target=main)
