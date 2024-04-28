import json
from typing import Union

from src.protocol.PacketData.PacketData import PacketData


class GetUserDocPacketData(PacketData):
    def __init__(self, data: Union[bytes, str]):
        super().__init__()

        if isinstance(data, bytes):
            self.packet_data = json.loads(data.decode())
            self.jwt_session = self.packet_data.get("jwt_session")
        else:
            self.jwt_session = data
            self.packet_data = {
                "jwt_session": self.jwt_session
            }

    def __bytes__(self):
        json_str = json.dumps(self.packet_data)
        return json_str.encode()

    def get_data(self):
        return self.packet_data.get("jwt_session")

if __name__ == '__main__':
    pass_data = GetUserDocPacketData("sdf")
    print(pass_data.get_data())
