__author__ = 'Ben'

from dataclasses import asdict
from socket import socket, AF_INET, SOCK_STREAM

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
        self.session_token = None
        self.key = None
        self.key_salt = None
        self.password =None
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
        packet_data = LoginPacketData(username=username, password=password)
        self.password = password
        packet = Packet(PacketType.LOGIN, bytes(packet_data))
        send_packet(self.client_socket, packet)

        packet = recv_packet(self.client_socket)
        if packet.packet_type == PacketType.SESSION:
            packet_data = SessionPacketData(bytes=packet.payload)
            self.session_token = packet_data.get_session_id()
            print("Login successful")
            print("jwt_token =", self.session_token)
            return True
        else:
            print("Login failed")
            return False

    def register(self, username: str, password: str, mail: str):
        packet_data = RegisterPacketData(username=username, password=password, mail=mail)
        packet = Packet(PacketType.REGISTER, bytes(packet_data))
        send_packet(self.client_socket, packet)

        packet = recv_packet(self.client_socket)
        if packet.packet_type == PacketType.SESSION:
            packet_data = SessionPacketData(bytes=packet.payload)
            self.session_token = packet_data.get_session_id()
            print("Login successful")
            return True
        else:
            print("Login failed")
            return False

    def add_pass(self, password: PasswordData):
        packet_data = AddItemPacketData(
            asdict(password), item_type="password", jwt_session=self.session_token
        )

        packet = Packet(PacketType.ADDITEM, bytes(packet_data))
        send_packet(self.client_socket, packet)
        print("Password added successfully")

    def delete_pass(self, password: PasswordData):
        packet_data = DeleteItemPacketData(
            asdict(password), item_type="password", jwt_session=self.session_token
        )

        packet = Packet(PacketType.DELETEITEM, bytes(packet_data))
        send_packet(self.client_socket, packet)
        print("Password deleted successfully")

    def add_pass(self, password: PasswordData):
        packet_data = AddItemPacketData(
            asdict(password), item_type="password", jwt_session=self.session_token
        )

        packet = Packet(PacketType.ADDITEM, bytes(packet_data))
        send_packet(self.client_socket, packet)
        print("Password added successfully")

    def get_user_data(self):
        packet_data = GetUserDocPacketData(self.session_token)
        packet = Packet(PacketType.GETUSERDOC, bytes(packet_data))
        send_packet(self.client_socket, packet)
        packet = recv_packet(self.client_socket)
        packet_data = PacketData(data=packet.payload)
        return packet_data.get_data()


if __name__ == '__main__':
    client = ClientConn('127.0.0.1', 3333)
    client.main()
    client.login("ben", "12345")

    password = PasswordData("https://www.niga.com", "ben", "12345", "12/12/2020")
    password2 = PasswordData("https://www.github.com", "ben", "niga", "12/12/2020")

    client.add_pass(password)
    client.add_pass(password2)

    items = client.get_user_data()

    print(items)
