import threading
from socket import socket

from src.protocol.Packet import HandelPacket, Packet
from src.protocol.PacketType import PacketType


class ServerConn:
    def __init__(self):
        pass
    def main(self):
        self.accept_connections()

    def accept_connections(self):
        self.server.listen()
        print(f'Listening... {self.addr}')
        while True:
            conn, addr = self.server.accept()
            threading.Thread(target=self.handel_connection, args=(conn, addr)).start()

    def handel_connection(self, conn: socket.socket, addr):
        packet = HandelPacket.recv_packet(conn)

        if packet.packet_type == PacketType.REGISTER:
          pass

        if packet.packet_type == PacketType.LOGIN:
            pass

    def handel_client(self, client):
      pass

    def handel_packet(self, packet: Packet):
        pass



