import flet as ft
from flet_core import Theme

THEME = Theme()
THEME.page_transitions.linux = ft.PageTransitionTheme.CUPERTINO
THEME.page_transitions.windows = ft.PageTransitionTheme.CUPERTINO
THEME.page_transitions.macos = ft.PageTransitionTheme.CUPERTINO
THEME.color_scheme = ft.ColorScheme(
    tertiary=ft.colors.WHITE,
    tertiary_container=ft.colors.BLACK,
    on_tertiary=ft.colors.BLACK,
    on_tertiary_container=ft.colors.BLACK,
)
THEME.dialog_theme = ft.DialogTheme(
    bgcolor=ft.colors.BACKGROUND,
    surface_tint_color=ft.colors.BACKGROUND
)
