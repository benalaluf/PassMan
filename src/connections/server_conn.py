import threading
from socket import socket

from src.protocol.Packet import Packet, recv_packet
from src.protocol.PacketData.LoginPacketData import LoginPacketData
from src.protocol.PacketType import PacketType


class ServerConn:
    def __init__(self, ip: str, port: int):
        self.addr = (ip, port)
        self.server_socket = socket()

    def init(self):
        self.server_socket.bind(self.addr)


    def main(self):
        self.init()
        self.accept_connections()

    def accept_connections(self):
        self.server_socket.listen()
        print(f'Listening... {self.addr}')
        while True:
            conn, addr = self.server_socket.accept()
            threading.Thread(target=self.handel_connection, args=(conn, addr)).start()

    def handel_connection(self, conn: socket, addr):
        packet = recv_packet(conn)

        if packet.packet_type == PacketType.REGISTER:
            pass

        if packet.packet_type == PacketType.LOGIN:
            packetData = LoginPacketData(bytes=packet.payload)
            self.login_user(conn, packetData)

    def handel_client(self, client):
        pass

    def handel_packet(self, packet: Packet):
        pass

    def login_user(self, conn: socket, packet: LoginPacketData):
        print(packet.data)

    def register_user(self, packet: Packet):
        pass


if __name__ == '__main__':
    server = ServerConn('127.0.0.1', 8080).main()
