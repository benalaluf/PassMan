import flet as ft


def LoginView(router):
    def exit_app(e):
        page = e.page
        page.window_destroy()
    def login(e):
        login
    content = ft.Column(
        [

            ft.Text("Login", size=30),
            ft.TextField(hint_text="Username"),
            ft.TextField(hint_text="Password"),
            ft.ElevatedButton(text="Login", on_click=login)
        ]

    )

    return content
