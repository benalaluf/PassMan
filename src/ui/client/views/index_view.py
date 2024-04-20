from typing import Union
import flet as ft

from src.ui.client.Data import State
from src.ui.client.views import Router
from src.ui.client.views.Router import DataStrategyEnum


def IndexView(r):
    def send_data(e: ft.ControlEvent):
        State("data", text_field.value)
        e.page.go("/data")

    text_field = ft.TextField()
    send_button = ft.ElevatedButton("Send")
    send_button.on_click = send_data
    content = ft.Column(
        [
            ft.Row(
                [
                    ft.Text(
                        "Welcome to my Flet Router Tutorial",
                        size=50),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    text_field,
                    send_button
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
    )

    return content
