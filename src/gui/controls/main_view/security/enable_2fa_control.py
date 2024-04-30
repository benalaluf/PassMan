import flet as ft

from src.connections.client_conn import ClientConn
from src.crypto.two_fa import generate_secret_token, generate_qr_code, verify_otp
from src.protocol.Packet.Packet import Packet, send_packet
from src.protocol.Packet.PacketType import PacketType
from src.protocol.PacketData.PacketData import PacketData


class EnableTwoFA(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = ft.Text("Enable 2FA", size=40, )
        self.qr_code = ft.Image(height=200, width=200)
        self.qr_button = ft.ElevatedButton(text="Generate QR Code", width=200)
        self.login_button = ft.ElevatedButton(text="Continue", width=200)
        self.code_field = ft.TextField(hint_text="Code",
                                       border=ft.InputBorder.UNDERLINE,
                                       label="Code",
                                       text_align=ft.TextAlign.CENTER,
                                       text_size=20,
                                       color=ft.colors.BLACK, )
        self.qr_button.on_click = self.qr_button_clicked
        self.login_button.on_click = self.login
        self.qr_code.visible = False
        self.login_button.visible = False
        self.code_field.visible = False

        self.login = ft.Container(ft.Column(
            [
                self.title,
                self.qr_button,
                self.qr_code,
                self.code_field,
                self.login_button
            ],
            width=400,
            height=400,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            border_radius=14,
            bgcolor=ft.colors.WHITE,
            padding=20,
            border=ft.border.all(color=ft.colors.BLACK, width=2),
        )

        self.content = ft.Container(
            self.login,
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.GREY_700
        )

    def qr_button_clicked(self, e):
        self.secret_key = generate_secret_token()

        # Generate a QR code for the secret key
        qr_code_filename = "qr_code.png"
        generate_qr_code(self.secret_key, qr_code_filename)
        self.qr_code.src = qr_code_filename
        self.qr_code.fit = ft.ImageFit.CONTAIN,
        self.qr_button.update()

        self.qr_button.visible = False
        self.qr_code.visible = True
        self.code_field.visible = True
        self.login_button.visible = True

        self.update()

    def login(self, e):
        result = verify_otp(self.secret_key, self.code_field.value)

        if result:
            print("OTP is valid")
            conn = ClientConn()
            conn.enable_2fa(self.secret_key)
            e.control.page.go('/main/security')
        print(result)

    def build(self):
        return self.content


if __name__ == '__main__':
    def main(page: ft.Page):
        page.add(EnableTwoFA())


    ft.app(target=main)
