import flet as ft
from views.routes import router
from src.ui.client.controls.app_bar import NavBar

def main(page: ft.Page):

    page.theme_mode = "light"
    page.appbar = NavBar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    page.go('/')

ft.app(target=main, assets_dir="assets")