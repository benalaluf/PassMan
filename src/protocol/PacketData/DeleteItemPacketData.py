import json
from typing import Union

from src.protocol.PacketData.PacketData import PacketData


class DeleteItemPacketData(PacketData):
    def __init__(self, data: Union[bytes, dict], item_type=None, jwt_session=None):
        super().__init__()

        if isinstance(data, bytes):
            self.packet_data = json.loads(data.decode())
            self.data = self.packet_data.get("data")
            self.item_type = self.packet_data.get("item_type")
            self.jwt_session = self.packet_data.get("jwt_session")
        else:
            self.data = data
            self.item_type = item_type
            self.jwt_session = jwt_session
            self.packet_data = {
                "item_type": self.item_type,
                "jwt_session": self.jwt_session,
                "data": self.data,
            }

    def __bytes__(self):
        json_str = json.dumps(self.packet_data)
        return json_str.encode()

    def get_data(self):
        return self.packet_data.get("data")


