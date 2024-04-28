import threading
from socket import socket

from pymongo import MongoClient

from src.crypto import hashing, jwt_session
from src.crypto.jwt_session import generate_secret_key

from src.protocol.Packet.Packet import Packet, send_packet, recv_packet
from src.protocol.Packet.PacketType import PacketType
from src.protocol.PacketData.AddItemPacketData import AddItemPacketData
from src.protocol.PacketData.LoginPacketData import LoginPacketData
from src.protocol.PacketData.RegisterPacketData import RegisterPacketData
from src.protocol.PacketData.SessionPacketData import SessionPacketData


class ServerConn:
    def __init__(self, server_addr, db_addr):
        self.server_addr = server_addr
        self.db_addr = db_addr

        self.server_socket = socket()
        self.init_connection()

        self.jwt_secret_key = generate_secret_key()

    def init_connection(self):
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

    def accept_connections(self):
        self.server_socket.listen()
        print(f'[+] Listening... {self.server_addr}')
        while True:
            conn, addr = self.server_socket.accept()
            print("got connection")
            threading.Thread(target=self.sdf, args=(conn,)).start()

    def sdf(self, conn: socket):
        while True:
            packet = recv_packet(conn)
            self.handel_packet(conn, packet)

    def handel_packet(self, conn: socket, packet: Packet):
        if packet.packet_type == PacketType.REGISTER:
            packetData = RegisterPacketData(bytes=packet.payload)
            self.register_user(conn, packetData)

        if packet.packet_type == PacketType.LOGIN:
            packetData = LoginPacketData(bytes=packet.payload)
            self.login_user(conn, packetData)

        if packet.packet_type == PacketType.ADDITEM:
            packetData = AddItemPacketData(packet.payload)
            if packetData.item_type == "password":
                self.add_password(conn, packetData)

    def login_user(self, conn: socket, packet: LoginPacketData):
        user = self.users_db.find_one({"username": packet.get_username()})
        if user is None:
            print("Login failed")
            return
        hash_pass = hashing.hashpass(packet.get_password(), user["pass_salt"])
        user = self.users_db.find_one({"username": packet.username, "password": hash_pass})
        if user:
            print("Login successful")
            self.send_session_token(conn, user["username"])
        else:
            print("Login failed")

    def register_user(self, conn: socket, packet: RegisterPacketData):
        data = packet.data
        key_salt = hashing.generate_salt()
        pass_salt = hashing.generate_salt()
        data["pass_salt"] = pass_salt
        data["key_salt"] = key_salt
        pass_hash = hashing.hashpass(packet.password, pass_salt)
        data["password"] = pass_hash
        self.users_db.insert_one(data)
        self.send_session_token(conn, data["username"])

    def add_password(self, conn: socket, packet: AddItemPacketData):
        user = jwt_session.verify_jwt(packet.jwt_session, self.jwt_secret_key)
        if user:
            data = packet.get_data()
            self.users_db.update_one({"username": user}, {"$push": {"items.passwords":data}}, upsert=True)

    def send_session_token(self, conn: socket, username: str):
        session_token = jwt_session.generate_jwt(username, self.jwt_secret_key)
        print(session_token)
        packetData = SessionPacketData(session_id=session_token)
        packet = Packet(PacketType.SESSION, bytes(packetData))
        send_packet(conn, packet)

    def handel_client(self, client):
        pass


if __name__ == '__main__':
    server = ServerConn(('127.0.0.1', 1231), ('127.0.0.1', 27017))
    server.accept_connections()
