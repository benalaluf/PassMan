import json
from typing import Union, Optional


class PacketData:
    def __init__(self, data: Union[bytes, dict]=None, jwt_session=None):
        super().__init__()

        if isinstance(data, bytes):
            self.packet_data = json.loads(data.decode())
            self.jwt_session = self.packet_data.get("jwt_session")
            self.data = self.packet_data.get("data")
        else:
            self.data = data
            self.jwt_session = jwt_session
            self.packet_data = {
                "jwt_session": self.jwt_session,
                "data": self.data,
            }

    def __bytes__(self):
        json_str = json.dumps(self.packet_data)
        return json_str.encode()

    def get_data(self):
        return self.data


if __name__ == '__main__':
    pass_data = PacketData({"url": "test", "username": "test", "password": "test", "date": "test"},
                                  jwt_session="test")
    print(pass_data.get_data())
