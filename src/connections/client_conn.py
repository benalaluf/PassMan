__author__ = 'Ben'

from dataclasses import asdict
from socket import socket, AF_INET, SOCK_STREAM

from src.crypto.aes import aes_encrypt, aes_decrypt
from src.crypto.pbkdf import generate_key_from_password
from src.data.conn.conn_user_data import ConnUserData
from src.data.db.card import CardData
from src.data.db.password import PasswordData
from src.data.packet_api.auth_data import AuthData
from src.data.packet_api.get_data import GetData
from src.data.packet_api.post_data import PostData
from src.misc.singletone import Singleton
from src.protocol.Packet import Packet, recv_packet, send_packet, send_and_recv_packet
from src.protocol.PacketType import PacketType
from src.protocol.PacketData import PacketData


class ClientConn(metaclass=Singleton):

    def __init__(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.user_data = ConnUserData()

    def connect_to_server(self, ip: str, port: int):
        try:
            self.client_socket.connect((ip, port))
            print(f'CONNECTED {(ip, port)}')
            self.connected = True

        except Exception as e:
            self.client_socket.close()
            print(e)
            exit(1)

    def login(self, username: str, password: str):
        data = AuthData(
            type="login",
            username=username,
            password=password
        )

        packet_data = PacketData(asdict(data))
        packet = Packet(PacketType.AUTH, bytes(packet_data))
        send_packet(self.client_socket, packet)

        response_packet = recv_packet(self.client_socket)
        if response_packet.packet_type == PacketType.SUCCESS:
            packet_data = PacketData(response_packet.payload)
            success_type = packet_data.get("type")
            if success_type == "auth":
                self.user_data.password = password
                self.user_data.username = username
                self.on_auth(packet_data)
                return "Success"
            else:
                self.user_data.password = password
                self.user_data.username = username
                return "2fa"

        else:
            print("Login failed")
            return "Fail"

    def two_fa(self, code):
        data = AuthData(
            type="2fa",
            username=self.user_data.username,
            two_fa_code=code,

        )

        packet_data = PacketData(asdict(data))
        packet = Packet(PacketType.AUTH, bytes(packet_data))

        response_packet = send_and_recv_packet(self.client_socket, packet)

        if response_packet.packet_type == PacketType.SUCCESS:
            packet_data = PacketData(response_packet.payload)
            success_type = packet_data.get("type")
            if success_type == "auth":
                self.on_auth(packet_data)
                return "Success"
            else:
                return "Fail"
        return "Fail"

    def register(self, username: str, password: str, mail: str):
        data = AuthData(
            type="register",
            username=username,
            password=password,
            mail=mail
        )

        packet_data = PacketData(asdict(data))
        packet = Packet(PacketType.AUTH, bytes(packet_data))

        response_packet = send_and_recv_packet(self.client_socket, packet)

        if response_packet.packet_type == PacketType.SUCCESS:
            packet_data = PacketData(response_packet.payload)
            self.user_data.password = password
            self.user_data.username = username
            self.on_auth(packet_data)
            return True
        else:
            print("Register failed")
            return False

    def on_auth(self, packet_data):
        data = packet_data.get("data")
        self.user_data.session = data.get("session")
        self.user_data.key_salt = data.get("key_salt")
        self.user_data.key = generate_key_from_password(self.user_data.password, self.user_data.key_salt)
        print("Login successful")
        print("jwt_token =", self.user_data.session)
        print("key_salt=", self.user_data.key_salt)

    def add_password(self, password: PasswordData):
        item_data = asdict(password)
        self.encrypt_item(item_data)
        data = PostData(
            session=self.user_data.session,
            type="add_item",
            item_type="password",
            data=item_data,
        )

        packet_data = PacketData(asdict(data))

        packet = Packet(PacketType.POST, bytes(packet_data))
        send_packet(self.client_socket, packet)
        print("sent add password")
        print(data.data)

    def add_card(self, card: CardData):
        item_data = asdict(card)
        self.encrypt_item(item_data)

        data = PostData(
            session=self.user_data.session,
            type="add_item",
            item_type="card",
            data=item_data,
        )

        packet_data = PacketData(
            asdict(data)
        )

        packet = Packet(PacketType.POST, bytes(packet_data))
        send_packet(self.client_socket, packet)
        print("sent add card")

    def delete_pass(self, password: PasswordData):
        data = PostData(
            session=self.user_data.session,
            type="delete_item",
            item_type="password",
            data=asdict(password),
        )

        packet_data = PacketData(
            asdict(data)
        )

        packet = Packet(PacketType.POST, bytes(packet_data))
        send_packet(self.client_socket, packet)
        print("sent delete successfully")

    def delete_card(self, card: CardData):
        data = PostData(
            session=self.user_data.session,
            type="delete_item",
            item_type="card",
            data=asdict(card),
        )

        packet_data = PacketData(
            asdict(data)
        )

        packet = Packet(PacketType.POST, bytes(packet_data))
        send_packet(self.client_socket, packet)
        print("sent delete successfully")

    def get_user_items(self):
        data = GetData(
            session=self.user_data.session,
            type="items"
        )

        packet_data = PacketData(asdict(data))
        packet = Packet(PacketType.GET, bytes(packet_data))
        response_packet = send_and_recv_packet(self.client_socket, packet)
        if response_packet.packet_type == PacketType.SUCCESS:
            packet_data = PacketData(response_packet.payload)
            encrypted_items = packet_data.get("data")
            self.decrypt_items(encrypted_items)
            print("[+] got items")
            return encrypted_items
        return None

    def enable_2fa(self, twofa_token):
        data = PostData(
            session=self.user_data.session,
            type="2fa",
            data={"two_fa_token":twofa_token}
        )
        packet_data = PacketData(asdict(data))
        packet = Packet(PacketType.POST, bytes(packet_data))
        send_packet(self.client_socket, packet)

    def decrypt_items(self, items: dict):
        for items_type in items.values():
            for item in items_type:
                self.decrypt_item(item)

    def encrypt_item(self, item):
        for k, value in item.items():
            if k == "id":
                continue
            item[k] = aes_encrypt(self.user_data.key, value)

    def decrypt_item(self, item):
        for k, value in item.items():
            if k == "id":
                continue
            item[k] = aes_decrypt(self.user_data.key, value)


if __name__ == '__main__':
    client = ClientConn()
    client.connect_to_server('127.0.0.1', 1233)
    niga = client.register("ben", "12345", "asdf")
    if niga:
        print("login")
    else:
        print("failed")

    password = PasswordData("https://www.niga.com", "ben", "12345", "12/12/2020")
    password2 = PasswordData("https://www.github.com", "ben", "niga", "12/12/2020")

    client.add_password(password)
    client.add_password(password2)

    items = client.get_user_items()
