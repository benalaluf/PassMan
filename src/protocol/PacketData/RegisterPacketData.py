import json

from src.protocol.PacketData.PacketData import PacketData


class RegisterPacketData(PacketData):

    def __init__(self, bytes=None, username=None, password=None, pass_salt=None, key_salt=None):
        super().__init__()
        if bytes:
            self.data = json.loads(bytes.decode())
            self.username = self.data.get("username")
            self.password = self.data.get("password")
            self.pass_salt = self.data.get("pass_salt")
            self.key_salt = self.data.get("key_salt")
        else:
            self.username = username
            self.password = password
            self.pass_salt = pass_salt
            self.key_salt = key_salt
            self.data = {
                "username": self.username,
                "password": self.password,
                "pass_salt": self.pass_salt,
                "key_salt": self.key_salt,
            }

    def get_data(self):
        return self.data

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_pass_salt(self):
        return self.pass_salt

    def get_key_salt(self):
        return self.key_salt
