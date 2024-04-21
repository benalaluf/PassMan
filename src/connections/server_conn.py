import binascii
import hashlib
import os
import threading
import pymongo
from socket import socket

from pymongo import MongoClient

from src.protocol.Packet import Packet, recv_packet
from src.protocol.PacketData.LoginPacketData import LoginPacketData
from src.protocol.PacketData.RegisterPacketData import RegisterPacketData
from src.protocol.PacketType import PacketType


class ServerConn:
    def __init__(self, server_addr, db_addr):
        self.server_addr = server_addr
        self.db_addr = db_addr
        self.server_socket = socket()
        self.init()

    def init(self):
        try:
            self.server_socket.bind(self.server_addr)
            print(f"[+] bind server ip to {self.server_addr} successfully")
            db_client = MongoClient(self.db_addr[0], self.db_addr[1])
            self.passman_db = db_client.PassMan
            self.users_db = self.passman_db.users
            print(f"[+] connected to db at {self.db_addr} successfully")
        except Exception as e:
            print("Server init faild", e)
            exit(1)

    def main(self):
        self.accept_connections()

    def accept_connections(self):
        self.server_socket.listen()
        print(f'[+] Listening... {self.server_addr}')
        while True:
            conn, addr = self.server_socket.accept()
            print("got connection")
            threading.Thread(target=self.handel_connection, args=(conn, addr)).start()

    def handel_connection(self, conn: socket, addr):
        while True:
            packet = recv_packet(conn)
            if packet.packet_type == PacketType.REGISTER:
                packetData = RegisterPacketData(bytes=packet.payload)
                self.register_user(conn, packetData)

            if packet.packet_type == PacketType.LOGIN:
                packetData = LoginPacketData(bytes=packet.payload)
                self.login_user(conn, packetData)

    def handel_client(self, client):
        pass

    def handel_packet(self, packet: Packet):
        pass

    def login_user(self, conn: socket, packet: LoginPacketData):
        data = packet.data
        user = self.users_db.find_one({"username": packet.username})
        hash_pass = self.hashpass(packet.password, user["pass_salt"])
        user = self.users_db.find_one({"username": packet.username, "password": hash_pass})
        if user:
            print("Login successful")
        else:
            print("Login failed")

    def register_user(self, conn: socket, packet: RegisterPacketData):
        data = packet.data
        key_salt = self.generate_salt()
        pass_salt = self.generate_salt()
        data["pass_salt"] = pass_salt
        data["key_salt"] = key_salt
        pass_hash = self.hashpass(packet.password, pass_salt)
        data["password"] = pass_hash
        self.users_db.insert_one(data)

    def hashpass(self, password, salt):
        to_hash = salt + password
        hash = hashlib.sha256(to_hash.encode()).hexdigest()
        return hash

    def generate_salt(self, length=16):
        # Generate raw bytes using a CSPRNG
        salt = os.urandom(length)
        # Encode the salt to a readable string (hexadecimal)
        encoded_salt = binascii.hexlify(salt).decode('utf-8')
        return encoded_salt


if __name__ == '__main__':
    server = ServerConn(('127.0.0.1', 8080), ('127.0.0.1', 27017))
    server.main()
