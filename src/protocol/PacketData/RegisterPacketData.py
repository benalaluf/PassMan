import json

from src.protocol.PacketData.PacketData import PacketData


class RegisterPacketData(PacketData):

    def __init__(self, bytes=None, username=None, password=None, mail=None):
        super().__init__()
        if bytes:
            self.data = json.loads(bytes.decode())
            self.username = self.data.get("username")
            self.password = self.data.get("password")
            self.mail = self.data.get("mail")
        else:
            self.username = username
            self.password = password
            self.mail = mail
            self.data = {
                "username": self.username,
                "password": self.password,
                "mail": self.mail,
            }
    def __bytes__(self):
        json_str = json.dumps(self.data)
        return json_str.encode()
    def get_data(self):
        return self.data

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_pass_salt(self):
        return self.mail
