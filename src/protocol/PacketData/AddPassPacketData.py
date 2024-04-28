import json

from src.protocol.PacketData.PacketData import PacketData


class AddPassPacketData(PacketData):
    def __init__(self, jwt_session=None,bytes=None, url=None, username=None, password=None, date=None):
        super().__init__()
        if bytes:
            self.data = json.loads(bytes.decode())
            self.jwt_session = self.data.get("jwt_session")
            self.url = self.data.get("url")
            self.username = self.data.get("username")
            self.password = self.data.get("password")
            self.date = self.data.get("date")
        else:
            self.jwt_session = jwt_session
            self.url = url
            self.username = username
            self.password = password
            self.date = date
            self.data = {
                "jwt_session": self.jwt_session,
                "url": self.url,
                "username": self.username,
                "password": self.password,
                "date": self.date
            }

    def __bytes__(self):
        json_str = json.dumps(self.data)
        return json_str.encode()

    def get_data(self):
        data = dict(self.data)
        data.pop("jwt_session")
        print(self.data)
        return data

    def get_url(self):
        return self.url

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_date(self):
        return self.date


if __name__ == '__main__':
    pass_data = AddPassPacketData(jwt_session="test", url="url", username="ben", password="1234", date="date")
    print(pass_data.get_data())