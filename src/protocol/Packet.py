import socket
import struct

from src.protocol.PacketConstants import PacketConstants
from src.protocol.PacketData import PacketData
from src.protocol.PacketType import PacketType


class Packet:
    def __init__(self, packet_type: PacketType, payload: bytes):
        self.packet_type = packet_type
        self.payload = payload
        self.packet_bytes = bytes()

    @classmethod
    def from_bytes(cls, data: bytearray):
        packet_type = PacketType(struct.unpack(PacketConstants.TYPE_HEADER_FORMAT, bytes(data[0:1]))[0])
        data_len = struct.unpack(PacketConstants.PAYLOAD_LENGTH_HEADER_FORMAT, bytes(data[1:5]))[0]
        payload = bytes(data[5:5 + data_len])

        return cls(packet_type, payload)

    def __bytes__(self):
        return self._build_packet()

    def _build_packet(self):
        self.packet_bytes = self._pack(PacketConstants.TYPE_HEADER_FORMAT, self.packet_type.value) + \
                            self._pack(PacketConstants.PAYLOAD_LENGTH_HEADER_FORMAT, (len(self.payload))) + \
                            self.payload
        return self.packet_bytes

    @staticmethod
    def _pack(pack_format: str, data):
        return struct.pack(pack_format, data)


def send_packet(sock: socket.socket, packet: Packet):
    sock.sendall(bytes(packet))


def recv_packet(sock):
    return Packet.from_bytes(__recv_raw_packet(sock))


def __recv_raw_packet(sock):
    raw_header = __recv_all(sock, PacketConstants.HEADER_LENGTH)

    if not raw_header:
        return None

    raw_data_len = raw_header[1:5]
    data_len = struct.unpack(PacketConstants.PAYLOAD_LENGTH_HEADER_FORMAT, raw_data_len)[0]
    data = __recv_all(sock, data_len)
    return raw_header + data


def __recv_all(sock, data_len):
    data = bytearray()
    while len(data) < data_len:
        packet = sock.recv(data_len - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data
