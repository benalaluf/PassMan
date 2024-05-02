__author__ = 'Ben'

import hashlib
from base64 import urlsafe_b64encode
from dataclasses import asdict
from socket import socket, AF_INET, SOCK_STREAM

from cryptography.fernet import Fernet

from src.crypto.aes import aes_encrypt, aes_decrypt
from src.crypto.pbkdf import generate_key_from_password
from src.data.items.card import CardData
from src.data.items.password import PasswordData
from src.misc.singletone import Singleton
from src.protocol.Packet.Packet import Packet, recv_packet, send_packet
from src.protocol.Packet.PacketType import PacketType
from src.protocol.PacketData.AddItemPacketData import AddItemPacketData
from src.protocol.PacketData.DeleteItemPacketData import DeleteItemPacketData
from src.protocol.PacketData.GetUserInfoPacketData import GetUserDocPacketData
from src.protocol.PacketData.LoginPacketData import LoginPacketData
from src.protocol.PacketData.PacketData import PacketData
from src.protocol.PacketData.RegisterPacketData import RegisterPacketData
from src.protocol.PacketData.SessionPacketData import SessionPacketData


class ClientConn(metaclass=Singleton):

    def __init__(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_items =None
        self.session_token = None
        self.key = None
        self.key_salt = None
        self.username = None
        self.password = None
        self.connected = False

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
        data = {
            "type": "login",
            "username": username,
            "password": password
        }

        packet_data = PacketData(data)
        packet = Packet(PacketType.AUTH, bytes(packet_data))
        send_packet(self.client_socket, packet)

        packet = recv_packet(self.client_socket)
        if packet.packet_type == PacketType.SUCCESS:
            packet_data = PacketData(packet.payload)
            success_type = packet_data.get("type")
            if success_type == "session":
                self.session_token = packet_data.get("data")
                print("Login successful")
                print("jwt_token =", self.session_token)
                self.password = password
                self.username = username
                self.get_user_key()
                return "Success"
            else:
                self.password = password
                self.username = username
                return "2fa"


        else:
            print("Login failed")
            return "Fail"

    def two_fa(self, code):
        data = {
            "type": "2fa",
            "code": code,
            "username": self.username
        }

        packet_data = PacketData(data)
        packet = Packet(PacketType.AUTH, bytes(packet_data))
        send_packet(self.client_socket, packet)

        packet = recv_packet(self.client_socket)
        if packet.packet_type == PacketType.SUCCESS:
            packet_data = PacketData(packet.payload)
            success_type = packet_data.get("type")
            if success_type == "session":
                self.session_token = packet_data.get("data")
                print("Login successful")
                print("jwt_token =", self.session_token)
                self.get_user_key()
                return "Success"
            else:
                return "Fail"
        return "Fail"

    def register(self, username: str, password: str, mail: str):

        data = {
            "type": "register",
            "username": username,
            "password": password,
            "mail": mail
        }

        packet_data = PacketData(data)
        packet = Packet(PacketType.AUTH, bytes(packet_data))
        send_packet(self.client_socket, packet)

        packet = recv_packet(self.client_socket)
        if packet.packet_type == PacketType.SUCCESS:
            print(packet.packet_type)
            packet_data = PacketData(packet.payload)
            print(packet_data.packet_data)
            self.session_token = packet_data.get("data")
            print("Register successful")
            self.password = password
            self.username = username
            self.get_user_key()
            return True
        else:
            print("Register failed")
            return False

    def add_password(self, password: PasswordData):
        item_data = asdict(password)
        self.encrypt_item(item_data)

        data = {
            "session": self.session_token,
            "type": "add_item",
            "item_type": "password",
            "item_data": item_data,
        }

        packet_data = PacketData(
            data
        )

        packet = Packet(PacketType.POST, bytes(packet_data))
        send_packet(self.client_socket, packet)
        print("sent add password")

    def add_card(self, card: CardData):
        item_data = asdict(card)
        self.encrypt_item(item_data)

        data = {
            "session": self.session_token,
            "type": "add_item",
            "item_type": "card",
            "item_data": item_data,
        }

        packet_data = PacketData(
            data
        )

        packet = Packet(PacketType.POST, bytes(packet_data))
        send_packet(self.client_socket, packet)
        print("sent add card")

    def delete_pass(self, password: PasswordData):
        data = {
            "session": self.session_token,
            "type": "delete_item",
            "item_type": "password",
            "item_data": asdict(password),
        }

        packet_data = PacketData(
            data
        )

        packet = Packet(PacketType.POST, bytes(packet_data))
        send_packet(self.client_socket, packet)
        print("sent delete successfully")

    def delete_card(self, card: CardData):
        data = {
            "session": self.session_token,
            "type": "delete_item",
            "item_type": "card",
            "item_data": asdict(card),
        }

        packet_data = PacketData(
            data
        )

        packet = Packet(PacketType.POST, bytes(packet_data))
        send_packet(self.client_socket, packet)
        print("sent delete successfully")

    def get_user_items(self):
        data = {
            "session": self.session_token,
            "type": "items"
        }

        packet_data = PacketData(data)
        packet = Packet(PacketType.GET, bytes(packet_data))
        send_packet(self.client_socket, packet)

        packet = recv_packet(self.client_socket)
        if packet.packet_type == PacketType.SUCCESS:
            packet_data = PacketData(packet.payload)
            print("got items")
            encrypted_items = packet_data.get("data")
            self.decrypt_items(encrypted_items)
            self.client_items = encrypted_items
            return encrypted_items
            print("didnt got items")
        return None

    def enable_2fa(self, twofa_token):
        data = {
            "session": self.session_token,
            "type": "2fa",
            "data": twofa_token
        }
        packet_data = PacketData(data)
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
            item[k] = aes_encrypt(self.key, value)

    def decrypt_item(self, item):
        for k, value in item.items():
            if k == "id":
                continue
            item[k] = aes_decrypt(self.key, value)

    def get_user_key(self):
        data = {
            "session": self.session_token,
            "type": "key_salt"
        }

        packet_data = PacketData(data)
        packet = Packet(PacketType.GET, bytes(packet_data))
        send_packet(self.client_socket, packet)

        packet = recv_packet(self.client_socket)
        if packet.packet_type == PacketType.SUCCESS:
            packet_data = PacketData(packet.payload)
            print("got key")
            self.key_salt = packet_data.get("data")
            print(self.key_salt)
            self.key = generate_key_from_password(self.password, self.key_salt)
            return packet_data.get("data")
            print("didnt got key")
        return None


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


