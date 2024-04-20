import flet as ft


def NavBar(page):
    NavBar = ft.AppBar(
        leading=ft.Icon(ft.icons.LOCK_PERSON),
        leading_width=70,
        title=ft.Text("PassMan"),
        center_title=False,
        bgcolor=ft.colors.RED,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
            ft.ElevatedButton(text="Register", on_click=lambda _: page.go('/register')),
            ft.ElevatedButton(text="Login", on_click=lambda _: page.go('/login'))
        ]
    )

    return NavBar
