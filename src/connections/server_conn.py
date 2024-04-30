import threading
from socket import socket

from pymongo import MongoClient

from src.crypto import hashing, jwt_session
from src.crypto.jwt_session import generate_secret_key

from src.protocol.Packet.Packet import Packet, send_packet, recv_packet
from src.protocol.Packet.PacketType import PacketType
from src.protocol.PacketData.AddItemPacketData import AddItemPacketData
from src.protocol.PacketData.DeleteItemPacketData import DeleteItemPacketData
from src.protocol.PacketData.GetUserInfoPacketData import GetUserDocPacketData
from src.protocol.PacketData.LoginPacketData import LoginPacketData
from src.protocol.PacketData.PacketData import PacketData
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
        packetData = PacketData(packet.payload)
        print(packetData.packet_data)
        if packet.packet_type == PacketType.LOGIN:
            self.login_user(conn, packetData)

        if packet.packet_type == PacketType.REGISTER:
            self.register_user(conn, packetData)

        if packet.packet_type == PacketType.POST:
            packetData = PacketData(packet.payload)
            type = packetData.get("type")

            if type == "add_item":
                self.add_item(conn, packetData)
            if type == "delete_item":
                self.delete_item(conn, packetData)

        if packet.packet_type == PacketType.GET:
            type = packetData.get("type")

            if type == "items":
                self.send_user_data(conn, packetData)
            if type == "key_salt":
                self.send_key_salt(conn, packetData)

    def login_user(self, conn: socket, packet: PacketData):
        username = packet.get("username")
        password = packet.get("password")

        user = self.users_db.find_one({"username": username})

        if user is None:
            print("Login failed")
            self.send_fail(conn, "login")
            return
        hash_pass = hashing.hashpass(password, user["pass_salt"])
        user = self.users_db.find_one({"username": username, "password": hash_pass})

        if user:
            print("Login successful")
            self.send_session_token(conn, user["username"])
        else:
            print("Login failed")
            self.send_fail(conn, "login")

    def register_user(self, conn: socket, packet: PacketData):
        data = packet.packet_data
        check_username = self.users_db.find_one({"username": data["username"]})
        print(check_username)
        if check_username is None:
            key_salt = hashing.generate_salt()
            pass_salt = hashing.generate_salt()
            data["pass_salt"] = pass_salt
            data["key_salt"] = key_salt
            pass_hash = hashing.hashpass(packet.get("password"), pass_salt)
            data["password"] = pass_hash
            self.users_db.insert_one(data)
            self.send_session_token(conn, data["username"])
            print("user register")
        self.send_fail(conn, "register")
        print("register failed")

    def send_session_token(self, conn: socket, username: str):
        session_token = jwt_session.generate_jwt(username, self.jwt_secret_key)
        data = {
            "type": "session",
            "data": session_token
        }
        packetData = PacketData(data)
        packet = Packet(PacketType.SUCCESS, bytes(packetData))
        send_packet(conn, packet)

    def add_item(self, conn: socket, packet: PacketData):
        session = packet.get("session")
        item_type = packet.get("item_type")
        item_data = packet.get("item_data")

        user = jwt_session.verify_jwt(session, self.jwt_secret_key)
        if user:
            print(item_data)

            existing_password = self.users_db.find_one({"username": user, f"items.{item_type}.id": item_data["id"]})

            if existing_password:
                self.users_db.update_one(
                    {"username": user, f"items.{item_type}.id": item_data["id"]},
                    {"$set": {f"items.{item_type}.$": item_data}}
                )
                print("Password object updated.")
            else:
                self.users_db.update_one(
                    {"username": user},
                    {"$push": {f"items.{item_type}": item_data}},
                    upsert=True
                )
                print("New password object added.")
        else:
            print("got unauthrized request")

    def delete_item(self, conn: socket, packet: PacketData):
        session = packet.get("session")
        item_type = packet.get("item_type")
        item_data = packet.get("item_data")

        user = jwt_session.verify_jwt(session, self.jwt_secret_key)
        if user:
            print(item_data)
            existing_password = self.users_db.update_one(
                {"username": user, f"items.{item_type}.id": item_data["id"]},
                {"$pull": {f"items.{item_type}": {"id": item_data["id"]}}}
            )

            print("deleted password object.", existing_password)
        print("got unauthrized request")


    def send_user_data(self, conn: socket, packet: PacketData):
        session = packet.get("session")

        username = jwt_session.verify_jwt(session, self.jwt_secret_key)
        user = self.users_db.find_one({"username": username})
        if user:
            if user.get("items"):
                user.pop("_id")
                data = {
                    "type": "items",
                    "data": user["items"]
                }
                packetData = PacketData(data)

                packet = Packet(PacketType.SUCCESS, bytes(packetData))
                send_packet(conn, packet)
            else:
                print("No items found")
                self.send_fail(conn, "items")


        print("got unauthrized request")


    def send_key_salt(self, conn: socket, packet: PacketData):
        session = packet.get("session")

        username = jwt_session.verify_jwt(session, self.jwt_secret_key)
        user = self.users_db.find_one({"username": username})
        if user:
            user.pop("_id")
            data = {
                "type": "key_salt",
                "data": user["key_salt"]
            }
            packetData = PacketData(data)

            packet = Packet(PacketType.SUCCESS, bytes(packetData))
            send_packet(conn, packet)

    def send_fail(self, conn: socket, fail_type: str):
        data = {
            "type": fail_type,
        }
        packetData = PacketData(data)
        packet = Packet(PacketType.FAIL, bytes(packetData))
        send_packet(conn, packet)

    def send_success(self, conn: socket, success_type: str, data):
        data = {
            "type": success_type,
            "data": data
        }
        packetData = PacketData(data)
        packet = Packet(PacketType.SUCCESS, bytes(packetData))
        send_packet(conn, packet)


if __name__ == '__main__':
    server = ServerConn(('127.0.0.1', 1233), ('127.0.0.1', 27017))
    server.accept_connections()
