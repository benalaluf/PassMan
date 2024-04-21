__author__ = 'Ben'

import binascii
import os
import threading
from socket import socket, AF_INET, SOCK_STREAM

from src.protocol.Packet import Packet, send_packet
from src.protocol.PacketData.LoginPacketData import LoginPacketData
from src.protocol.PacketData.RegisterPacketData import RegisterPacketData
from src.protocol.PacketType import PacketType


class ClientConn:

    def __init__(self, ip: str, port: int):
        self.server_addr = (ip, port)
        self.client_socket = socket(AF_INET, SOCK_STREAM)

    def main(self):
        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.client_socket.connect(self.server_addr)
            print(f'CONNECTED {self.server_addr}')
            self.connected = True

        except Exception as e:
            self.client_socket.close()
            print(e)
            exit(1)



    def login(self, username: str, password: str):
        packet_data = LoginPacketData(username=username, password=password)
        packet = Packet(PacketType.LOGIN, bytes(packet_data))
        send_packet(self.client_socket, packet)

    def register(self, username: str, password: str, mail: str):
        packet_data = RegisterPacketData(username=username, password=password, mail=mail)
        packet = Packet(PacketType.REGISTER, bytes(packet_data))
        send_packet(self.client_socket, packet)


if __name__ == '__main__':
    client = ClientConn('127.0.0.1', 8080).main()
